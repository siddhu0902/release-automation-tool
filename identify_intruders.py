#identify intruders
def identify_intruders(attempts, authorized):
    result = set()
    for user in attempts:
        if user not in authorized:
            result.add(user)
    return result
login_attempts = [" alice ", "bob", " mallory ", " frank ", " eve "]
authorized_users = {" alice ", "bob", " frank ", " grace "}
print(identify_intruders(login_attempts, authorized_users))
