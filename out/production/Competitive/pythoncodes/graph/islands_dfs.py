def dfs(r, c, mat, visited):
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]):
        return

    if mat[r][c] == 0:
        return

    mat[r][c] = 0

    dfs(r, c - 1, mat, visited)
    dfs(r, c + 1, mat, visited)
    dfs(r - 1, c, mat, visited)
    dfs(r + 1, c, mat, visited)


def social_network(r, c, strings, visited):
    if r < 0 or r >= len(strings) or c < 0 or c >= len(strings[0]) or str(r) + str(c) in visited:
        return

    if strings[r][c] == '0':
        return

    visited.add(str(r) + str(c))
    social_network(r, c - 1, strings, visited)
    social_network(r, c + 1, strings, visited)
    social_network(r - 1, c, strings, visited)
    social_network(r + 1, c, strings, visited)


if __name__ == "__main__":
    mat = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

    visit = set()
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                dfs(i, j, mat, visit)
                count += 1

    print(count)

    count = 0
    visit = set()
    strs = ['110', '110', '001']
    for i in range(len(strs)):
        for j in range(len(strs[i])):
            if strs[i][j] == '1' and str(i) + str(j) not in visit:
                social_network(i, j, strs, visit)
                count += 1

    print(count)
