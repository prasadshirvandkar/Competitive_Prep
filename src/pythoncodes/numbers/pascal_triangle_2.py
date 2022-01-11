def pascalTriangle(ind: int, row: int, pt):
    res = [1 for _ in range(ind + 1)]
    for p in range(1, ind):
        res[p] = pt[p - 1] + pt[p]
    res[ind] = 1

    if ind == row:
        return res

    return pascalTriangle(ind + 1, row, res)


def getRow(rowIndex: int):
    if rowIndex == 0:
        return [1]

    pt = [1, 1]
    if rowIndex == 1:
        return pt

    return pascalTriangle(2, rowIndex, pt)


if __name__ == '__main__':
    print(getRow(5))
