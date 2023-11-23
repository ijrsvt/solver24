def permutations(lst):
    return permutations_r([[]], lst)


def permutations_r(lst, remaining):
    if len(remaining) == 0:
        return lst
    remaining = remaining.copy()
    result = []
    for i, v in enumerate(remaining):
        cp = remaining.copy()
        cp.pop(i)
        result += permutations_r([l + [v] for l in lst], cp)
    return result
