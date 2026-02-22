"""A pytest plugin useful to test tox itself (and its plugins)."""

from __future__ import annotations

import inspect
import os
import re
import shutil
import socket
import sys
import textwrap
import warnings
from contextlib import closing, contextmanager
from pathlib import Path
from types import ModuleType, TracebackType
from typing import TYPE_CHECKING, Any, Protocol, cast

import pytest
from _pytest.fixtures import SubRequest  # noqa: PLC2701
from devpi_process import IndexServer
from virtualenv.info import fs_supports_symlink

import tox.run
from tox.execute.api import Execute, ExecuteInstance, ExecuteOptions, ExecuteStatus, Outcome
from tox.execute.request import ExecuteRequest, shell_cmd
from tox.plugin import manager
from tox.report import LOGGER, OutErr
from tox.run import run as tox_run
from tox.run import setup_state as previous_setup_state
from tox.session.cmd.run.parallel import ENV_VAR_KEY
from tox.tox_env import api as tox_env_api
from tox.tox_env.api import ToxEnv

if TYPE_CHECKING:                                  #Ensure_logging_framework_not_altered: fixture to ensure
    from collections.abc import Callable, Iterator, Sequence    #no test alters the logging framework configuration
    from unittest.mock import MagicMock

    from pytest_mock import MockerFixture

    from tox.config.sets import EnvConfigSet        #_disable_root_tox: fixture that blocks loading toxfile.py 
    from tox.execute.stream import SyncWrite        #if not a pluggin.py. prevents acc use of real file
    from tox.session.state import State

    CaptureFixture = pytest.CaptureFixture[str]
    MonkeyPatch = pytest.MonkeyPatch
    TempPathFactory = pytest.TempPathFactory
    LogCaptureFixture = pytest.LogCaptureFixture

os.environ["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
os.environ["PIP_NO_PYTHON_VERSION_WARNING"] = "1"

if fs_supports_symlink():  # pragma: no cover # used to speed up test suite run time where possible
    os.environ["VIRTUALENV_SYMLINK_APP_DATA"] = "1"
    os.environ["VIRTUALENV_SYMLINKS"] = "1"


@pytest.fixture(autouse=True)               #check_os_envin: context manager to ensure no test alters os.environ,clean tox,fails:extra or missing
def ensure_logging_framework_not_altered() -> Iterator[None]:
    before_handlers = list(LOGGER.handlers)
    yield
    LOGGER.handlers = before_handlers


@pytest.fixture(autouse=True)           #same_stable: fixture tht runs each test in check_os_environ. then undergoes monkeypatch 
def _disable_root_tox_py(request: SubRequest, mocker: Any) -> Iterator[None]:   #to keep it stable b/w tests
    """Unless this is a plugin test do not allow loading toxfile.py."""
    if request.node.get_closest_marker("plugin_test"):  # unregister inline plugin
        module, load_inline = None, manager._load_inline  # noqa: SLF001

        def _load_inline(path: Path) -> ModuleType | None:  # register only on first run, and unregister at end
            nonlocal module                     #it is a object representing a temp tox project (basically directory)
            module = load_inline(path)          #used for creating files and run tox cmds in that dir
            return module           #no_color:  fixture to set NO_COLOR in os.environ for each test
                                                            #APSI: color codings
        mocker.patch.object(manager, "_load_inline", _load_inline)
        yield
        if module is not None:  # pragma: no branch
            manager.MANAGER.manager.unregister(module)
    else:  # do not allow loading inline plugins
        mocker.patch("tox.plugin.inline._load_plugin", return_value=None)
        yield


@contextmanager                 #static method to convert nested dictionary to real external commands
def check_os_environ() -> Iterator[None]:
    old = os.environ.copy()
    to_clean = {
        k: os.environ.pop(k, None)
        for k in (ENV_VAR_KEY, "TOX_WORK_DIR", "PYTHONPATH", "COV_CORE_CONTEXT", "TOX_DISABLED_EXTERNAL_PLUGINS")
    }

    yield

    for key, value in to_clean.items():
        if value is not None:
            os.environ[key] = value

    new = os.environ                #Toxproject.patch_execute: method to patch ToxEnv._execute_call to use mock executor so test can run without
    extra = {k: new[k] for k in set(new) - set(old)}          #running ext cmds
    extra.pop("PLAT", None)
    extra.pop("TOX_DISABLED_EXTERNAL_PLUGINS", None)
    miss = {k: old[k] for k in set(old) - set(new)}
    diff = {
        f"{k} = {old[k]} vs {new[k]}" for k in set(old) & set(new) if old[k] != new[k] and not k.startswith("PYTEST_")
    }
    if extra or miss or diff:
        msg = "test changed environ"
        if extra:
            msg += f" extra {extra}"
        if miss:
            msg += f" miss {miss}"
        if diff:
            msg += f" diff {diff}"
        pytest.fail(msg)


@pytest.fixture(autouse=True)
def check_os_environ_stable(monkeypatch: Any) -> Iterator[None]:
    with check_os_environ():
        yield
        monkeypatch.undo()


@pytest.fixture(autouse=True)
def no_color(monkeypatch: Any, check_os_environ_stable: None) -> None:  # noqa: ARG001
    monkeypatch.setenv("NO_COLOR", "yes")


class ToxProject:               #ToxProject.Structure:property tht converts directory to dictionaries and file contents for assertions 
    def __init__(  # noqa: PLR0913
        self,
        files: dict[str, Any],
        base: Path | None,
        path: Path,
        capfd: Any,
        monkeypatch: Any,
        mocker: Any,
    ) -> None:
        self.path: Path = path
        self.monkeypatch: Any = monkeypatch
        self.mocker = mocker
        self._capfd = capfd
        self._setup_files(self.path, base, files)

    @staticmethod
    def _setup_files(dest: Path, base: Path | None, content: dict[str, Any]) -> None:       #ToxProject.chdir:contxxt manager
        if base is not None:
            shutil.copytree(str(base), str(dest))
        dest.mkdir(exist_ok=True)
        for key, value in content.items():
            if not isinstance(key, str):
                msg = f"{key!r} at {dest}"
                raise TypeError(msg)  # pragma: no cover
            at_path = dest / key
            if callable(value):
                value = textwrap.dedent("\n".join(inspect.getsourcelines(value)[0][1:]))  # noqa: PLW2901
                value = f"from __future__ import annotations\n{value}"  # noqa: PLW2901
            if isinstance(value, dict):
                at_path.mkdir(exist_ok=True)
                ToxProject._setup_files(at_path, None, value)
            elif isinstance(value, str):
                at_path.write_text(textwrap.dedent(value), encoding="utf-8")
            elif value is None:
                at_path.mkdir()
            else:
                msg = f"could not handle {at_path / key} with content {value!r}"  # pragma: no cover
                raise TypeError(msg)  # pragma: no cover

    def patch_execute(self, handle: Callable[[ExecuteRequest], int | None] | None = None) -> Any:  # noqa: C901
        class MockExecute(Execute):                  #ToxPreject.run: config. tox's state and sys.arg to run tox commands in this project dir
            def __init__(self, colored: bool, exit_code: int) -> None:  #returns a tox outcome with captured output and state
                self.exit_code = exit_code
                super().__init__(colored)

            def build_instance(
                self,
                request: ExecuteRequest,
                options: ExecuteOptions,
                out: Any,
                err: Any,
            ) -> ExecuteInstance:
                return MockExecuteInstance(request, options, out, err, self.exit_code)

        class MockExecuteStatus(ExecuteStatus):                  #Lightweight holder, stores "code,output,errors and state" from a tox cmd execution
            def __init__(self, options: ExecuteOptions, out: Any, err: Any, exit_code: int) -> None:
                super().__init__(options, out, err)
                self._exit_code = exit_code

            @property
            def exit_code(self) -> int | None:
                return self._exit_code

            def wait(self, timeout: float | None = None) -> int | None:  # noqa: ARG002
                return self._exit_code

            def write_stdin(self, content: str) -> None:  # noqa: ARG002, PLR6301
                return None  # pragma: no cover

            def interrupt(self) -> None:  # noqa: PLR6301
                return None  # pragma: no cover

        class MockExecuteInstance(ExecuteInstance):
            def __init__(
                self,
                request: ExecuteRequest,
                options: ExecuteOptions,
                out: Any,
                err: Any,
                exit_code: int,
            ) -> None:
                super().__init__(request, options, out, err)
                self.exit_code = exit_code

            def __enter__(self) -> ExecuteStatus:
                return MockExecuteStatus(self.options, self._out, self._err, self.exit_code)

            def __exit__(
                self,
                exc_type: type[BaseException] | None,
                exc_val: BaseException | None,
                exc_tb: TracebackType | None,
            ) -> None:
                pass

            @property
            def cmd(self) -> Sequence[str]:
                return self.request.cmd

        @contextmanager
        def _execute_call(
            self: ToxEnv,
            executor: Execute,
            out_err: OutErr,
            request: ExecuteRequest,
            show: bool,  # noqa: FBT001
        ) -> Iterator[ExecuteStatus]:
            exit_code = 0 if handle is None else handle(request)
            if exit_code is not None:
                executor = MockExecute(colored=executor._colored, exit_code=exit_code)  # noqa: SLF001
            with original_execute_call(self, executor, out_err, request, show) as status:
                yield status

        original_execute_call = ToxEnv._execute_call  # noqa: SLF001
        return self.mocker.patch.object(ToxEnv, "_execute_call", side_effect=_execute_call, autospec=True)

    @property
    def structure(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for dir_name, _, files in os.walk(str(self.path)):
            dir_path = Path(dir_name)
            into = result
            relative = dir_path.relative_to(str(self.path))
            for elem in relative.parts:
                into = into.setdefault(elem, {})
            for file_name in files:
                into[file_name] = (dir_path / file_name).read_text()
        return result

    @contextmanager
    def chdir(self, to: Path | None = None) -> Iterator[None]:
        cur_dir = Path.cwd()
        os.chdir(to or self.path)
        try:
            yield
        finally:
            os.chdir(cur_dir)

    def run(self, *args: str, from_cwd: Path | None = None, raise_on_config_fail: bool = True) -> ToxRunOutcome:
        if raise_on_config_fail and args and args[0] in {"c", "config"}:
            self.monkeypatch.setenv("_TOX_SHOW_CONFIG_RAISE", "1")

        with self.chdir(from_cwd):
            self._capfd.readouterr()  # start with a clean state - drain
            code = None
            state = None

            def our_setup_state(value: Sequence[str]) -> Any:
                nonlocal state
                state = previous_setup_state(value)
                return state

            with self.monkeypatch.context() as m:
                m.setattr(tox_env_api, "_CWD", self.path)
                m.setattr(tox.run, "setup_state", our_setup_state)
                m.setattr(sys, "argv", [sys.executable, "-m", "tox", *list(args)])
                m.setenv("VIRTUALENV_SYMLINK_APP_DATA", "1")
                m.setenv("VIRTUALENV_SYMLINKS", "1")
                m.setenv("VIRTUALENV_PIP", "embed")
                m.setenv("VIRTUALENV_SETUPTOOLS", "embed")
                try:
                    tox_run(args)
                except SystemExit as exception:
                    code = exception.code
                if code is None:
                    pytest.fail("tox did not call sys.exit")
                return ToxRunOutcome(
                    code=code,
                    out_err=self._capfd.readouterr(),
                    state=cast("State", state),
                )


class ToxRunOutcome:
    def __init__(self, code: int, out_err: tuple[str, str], state: State) -> None:
        self.code = code
        self.out = out_err[0]
        self.err = out_err[1]
        self.state = state
