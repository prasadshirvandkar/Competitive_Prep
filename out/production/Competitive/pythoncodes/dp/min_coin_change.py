def min_coin__change():
    coins = [1, 2, 5]
    amount = 11

    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0

    for i in range(0, 12):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i - c] + 1, dp[i])
                if i - c == 0:
                    break

    print(dp)


def unique_ways_of_coins_change():
    coins = [1, 2, 5]
    amount = 6

    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

    for i in range(0, len(dp)):
        for j in range(0, len(dp[0])):
            if i == 0:
                dp[i][j] = 1

            if j == 0:
                dp[i][j] = 0
                continue

            if j - coins[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

    print(dp)


if __name__ == "__main__":
    min_coin__change()
    unique_ways_of_coins_change()
