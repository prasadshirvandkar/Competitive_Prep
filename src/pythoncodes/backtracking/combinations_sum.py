def backtrack(combinations, target, temp, res, ind):
    if sum(temp) > target:
        return

    for i in range(ind, len(combinations)):
        temp.append(combinations[i])
        if sum(temp) == target:
            res.append([tmp for tmp in temp])
        else:
            backtrack(combinations, target, temp, res, i)
        temp.pop(-1)
    return res


def combinations_sum(combinations, target):
    return backtrack(combinations, target, [], [], 0)


if __name__ == '__main__':
    c = [2, 3, 6, 7]
    t = 7
    c1 = [2, 3, 5]
    t1 = 8
    print(combinations_sum(c, t))
    print(combinations_sum(c1, t1))
    print(combinations_sum([2], 1))
