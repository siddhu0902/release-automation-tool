# Expression Tree Builder & Evaluator (No imports, No games!)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def precedence(op):
    if op in ["+", "-"]:
        return 1
    if op in ["*", "/"]:
        return 2
    if op == "^":
        return 3
    return 0

def is_operator(c):
    return c in "+-*/^"

def build_tree(expr):
    # Remove outer parentheses
    expr = expr.strip()
    while expr.startswith("(") and expr.endswith(")") and matching_parentheses(expr):
        expr = expr[1:-1].strip()

    # Find the operator with lowest precedence not in parentheses
    min_prec = 100
    op_pos = -1
    paren_depth = 0
    for i in range(len(expr)):
        if expr[i] == '(':
            paren_depth += 1
        elif expr[i] == ')':
            paren_depth -= 1
        elif is_operator(expr[i]) and paren_depth == 0:
            prec = precedence(expr[i])
            if prec <= min_prec:
                min_prec = prec
                op_pos = i
    if op_pos == -1:
        return Node(expr)
    left = build_tree(expr[:op_pos])
    right = build_tree(expr[op_pos+1:])
    return Node(expr[op_pos], left, right)

def matching_parentheses(expr):
    depth = 0
    for i in range(len(expr)):
        if expr[i] == '(':
            depth += 1
        elif expr[i] == ')':
            depth -= 1
            if depth == 0 and i != len(expr)-1:
                return False
    return depth == 0

def evaluate(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        try:
            return float(node.val)
        except ValueError:
            print(f"Error: Unknown value '{node.val}'")
            return 0
    lval = evaluate(node.left)
    rval = evaluate(node.right)
    if node.val == "+":
        return lval + rval
    if node.val == "-":
        return lval - rval
    if node.val == "*":
        return lval * rval
    if node.val == "/":
        if rval == 0:
            print("Error: Divide by zero")
            return float('inf')
        return lval / rval
    if node.val == "^":
        return lval ** rval
    return 0

def print_tree(node, indent="", pos="root"):
    if node:
        print(indent, pos, ":", node.val)
        indent += "   "
        print_tree(node.left, indent, "L")
        print_tree(node.right, indent, "R")

print("Expression Tree Builder & Evaluator (No imports, No games!)")
print("Enter a math expression (e.g., (2+3)*5-2^3). Type 'quit' to exit.\n")

while True:
    expr = input("Expr: ")
    if expr.lower() == "quit":
        print("Bye!")
        break
    tree = build_tree(expr)
    print("\nExpression tree:")
    print_tree(tree)
    result = evaluate(tree)
    print("Result:", result)