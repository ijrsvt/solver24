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


def solve(*args, goal=24.0):
    assert len(args) == 4, "Only allowed 4 args"
    combos = [list(i) for i in set(tuple(x) for x in combine(list(args)))]

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

    return list(filter(lambda x: np.isclose(safe_eval(x), 24.0), possibilities))


assert all(
    [
        solve(6, 1, 3, 4),
        solve(3, 6, 6, 11),
        solve(3, 5, 7, 13),
        solve(2, 5, 5, 10),
        solve(2, 3, 5, 12),
        solve(12, 2, 1, 1),
        solve(8, 1, 1, 1),
    ]
)
