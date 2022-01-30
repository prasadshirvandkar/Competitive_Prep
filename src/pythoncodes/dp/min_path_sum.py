def min_path_sum(paths):
    dp = [[0 for _ in range(len(paths[0]))] for _ in range(len(paths))]

    for i in range(0, len(paths)):
        for j in range(0, len(paths[0])):
            if i == 0:
                dp[i][j] = paths[i][j] + dp[i][j - 1]
            elif j == 0:
                dp[i][j] = paths[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = paths[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 10],
        [4, 2, 1]
    ]

    grid1 = [[1, 3, 2]]

    grid2 = [
        [1, 3, 1],
        [1, 5, 14],
        [4, 2, 1],
        [15, 4, 1]
    ]

    print(min_path_sum(grid2))
