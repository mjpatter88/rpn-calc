from collections import deque
import operator
import math

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}

def calc(expr):
    if expr == "":
        return 0

    stack = deque()

    parts = expr.split(" ")
    for part in parts:
        if part in operators:
            a = stack.pop()
            b = stack.pop()
            op = operators[part]
            stack.append(op(b, a))
        else:
            stack.append(int(part))

    return stack.pop()
