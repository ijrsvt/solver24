import numpy as np

operations = ["+", "-", "*", "/"]


def safe_eval(expr):
    try:
        return eval(expr)
    except (ZeroDivisionError, NameError):
        return float("nan")


def combine(lst):
    return combine_r([[]], lst)


def combine_r(lst, remaining):
    if len(remaining) == 0:
        return lst
    remaining = remaining.copy()
    result = []
    for i, v in enumerate(remaining):
        cp = remaining.copy()
        cp.pop(i)
        result += combine_r([l + [v] for l in lst], cp)
    return result


def solve(a, b, c, d, goal=24.0):
    combos = [list(i) for i in set(tuple(x) for x in combine([a, b, c, d]))]

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
