I = [[1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 1, 1, 0],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0]]

count = []


def dfs(i, j, rows, cols):
    if i < 0 or j < 0 or i > rows or j > cols or I[i][j] != 1:
        return
    count.append(1)
    I[i][j] = 0
    dfs(i, j - 1, rows, cols)
    dfs(i, j + 1, rows, cols)
    dfs(i - 1, j, rows, cols)
    dfs(i + 1, j, rows, cols)


def count_ones():
    for i in range(len(I)):
        for j in range(len(I[0])):
            if I[i][j] == 1:
                dfs(i, j, len(I) - 1, len(I[0]) - 1)

    print(sum(count))


if __name__ == '__main__':
    count_ones()