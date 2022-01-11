arr = [1, 2, 3, 4, 5, 6]
s = 3


def sub_sum():
    dp = [[False for _ in range(s + 1)] for _ in range(len(arr))]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if j == 0:
                dp[i][j] = True
            elif j < arr[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i]]

    print(dp)


def count_sub_sum():
    dp = [[0 for _ in range(s + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if j == 0:
                dp[i][j] = 1
            elif j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]

    for d in dp:
        print(d)


if __name__ == "__main__":
    # sub_sum()
    count_sub_sum()
