from itertools import permutations
import numpy as np


operations = ["+", "-", "*", "/"]


def safe_eval(expr):
    try:
        return eval(expr)
    except (ZeroDivisionError, NameError):
        return float("nan")


def solve(a, b, c, d, goal=24.0):
    combos = [list(i) for i in set(permutations([a, b, c, d]))]

    possibilities = [
        [
            f"((({c[0]} {op1} {c[1]}) {op2} {c[2]}) {op3} {c[3]})",
            f"({c[0]} {op1} ({c[1]} {op2} ({c[2]} {op3} {c[3]})))",
            f"(({c[0]} {op1} {c[1]}) {op2} ({c[2]} {op3} {c[3]}))",
            f"(({c[0]} {op1} ({c[1]} {op2} {c[2]})) {op3} {c[3]})",
            f"({c[0]} {op1} (({c[1]} {op2} {c[2]}) {op3} {c[3]}))",
        ]
        for c in combos
        for op1 in operations
        for op2 in operations
        for op3 in operations
    ]
    possibilities = [p for tpl in possibilities for p in tpl]

    return list(filter(lambda x: np.isclose(safe_eval(x), goal), possibilities))
