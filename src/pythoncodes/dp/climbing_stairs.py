def climbing_stars(n):
    if n == 1:
        return 1

    dp = [1, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 2] + dp[i - 1])

    return dp[-1]


def climbing_stairs_rec(n):
    if n < 0:
        return 0

    if n == 0 or n == 1:
        return 1

    return climbing_stairs_rec(n - 1) + climbing_stairs_rec(n - 2)


if __name__ == '__main__':
    stairs = 3
    print(climbing_stars(stairs))
    print(climbing_stairs_rec(stairs))
