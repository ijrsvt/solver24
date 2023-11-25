import concurrent.futures
from itertools import permutations
import numpy as np


operations = ["+", "-", "*", "/"]


def safe_eval(expr):
    try:
        return eval(expr)
    except (ZeroDivisionError, NameError):
        return float("nan")


def _all_operations(numbers, goal) -> list:
    c = numbers
    def _permutations():
        for op1 in operations:
            for op2 in operations:
                for op3 in operations:
                    yield from (
            f"((({c[0]} {op1} {c[1]}) {op2} {c[2]}) {op3} {c[3]})",
            f"({c[0]} {op1} ({c[1]} {op2} ({c[2]} {op3} {c[3]})))",
            f"(({c[0]} {op1} {c[1]}) {op2} ({c[2]} {op3} {c[3]}))",
            f"(({c[0]} {op1} ({c[1]} {op2} {c[2]})) {op3} {c[3]})",
            f"({c[0]} {op1} (({c[1]} {op2} {c[2]}) {op3} {c[3]}))",
                    )
    return filter(lambda x: np.isclose(safe_eval(x), goal), _permutations())

def solve(a, b, c, d, goal=24.0):
    combos = [list(i) for i in set(permutations([a, b, c, d]))]
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        for result in executor.map(lambda c : list(_all_operations(c, goal=goal)), combos):
            results.extend(result)
    return results
            

