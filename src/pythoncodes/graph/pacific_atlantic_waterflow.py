def dfs(r, c, prev, heights, visited):
    if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]):
        return

    if prev > heights[r][c] or str(r) + str(c) in visited:
        return

    visited.add(str(r) + str(c))

    dfs(r, c - 1, heights[r][c], heights, visited)
    dfs(r, c + 1, heights[r][c], heights, visited)
    dfs(r - 1, c, heights[r][c], heights, visited)
    dfs(r + 1, c, heights[r][c], heights, visited)


def pacific_atlantic_waterflow(heights):
    pacific_visited = set()
    atlantic_visited = set()

    column = False
    for i in range(0, 2):
        for j in range(0, len(heights)):
            r = j if column else 0
            c = 0 if column else j
            if heights[r][c] not in pacific_visited:
                dfs(r, c, heights[r][c], heights, pacific_visited)
            column = True

    pacific_visited.add(str(len(heights) - 1) + str(0))
    pacific_visited.add(str(0) + str(len(heights) - 1))

    column = False
    for i in range(0, 2):
        for j in range(0, len(heights)):
            r = j if column else len(heights) - 1
            c = len(heights) - 1 if column else j
            if heights[r][c] not in atlantic_visited:
                dfs(r, c, heights[r][c], heights, atlantic_visited)
            column = True

    atlantic_visited.add(str(0) + str(len(heights) - 1))

    res = [value for value in pacific_visited if value in atlantic_visited]
    return [[int(r[0]), int(r[1])] for r in res]


if __name__ == '__main__':
    h = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]

    h1 = [[2, 1], [1, 2]]

    print(pacific_atlantic_waterflow(h))
