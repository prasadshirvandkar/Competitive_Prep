weights = [5, 3, 4, 2]
values = [60, 50, 70, 30]
max_weight = 5


def knapsack():
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(len(weights))]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])

    print(dp)


if __name__ == "__main__":
    knapsack()
