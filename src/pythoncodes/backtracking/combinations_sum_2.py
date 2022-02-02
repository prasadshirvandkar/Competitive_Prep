def backtrack(combinations, target, curr, res, ind):
    if sum(curr) > target:
        return

    for i in range(ind, len(combinations)):
        curr.append(combinations[i])
        if sum(curr) == target and curr not in res:
            res.append([comb for comb in curr])
        else:
            backtrack(combinations, target, curr, res, i + 1)
        curr.pop(-1)
    return res


def combinations_sum_2(combinations, target):
    combinations.sort()
    return backtrack(combinations, target, [], [], 0)

"""
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""

if __name__ == '__main__':
    c = [10, 1, 2, 7, 6, 1, 5]
    t = 8
    c2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    t2 = 27
    print(combinations_sum_2(c, t))
    print(combinations_sum_2(c2, t2))
