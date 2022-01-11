def target_sum(nums, target):
    n = len(nums)
    dp = [[0 for _ in range(target + 1)] for _ in range(1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        i_dp = []
        for j in range(0, target + 1):
            if j == 0:
                i_dp.append(1)
            elif j < nums[i - 1]:
                i_dp.append(dp[i - 1][j])
            else:
                i_dp.append(dp[i - 1][j] + dp[i - 1][j - nums[i - 1]])
        dp.append(i_dp)

    for d in dp:
        print(d)


if __name__ == '__main__':
    arr = [1]
    t = 1
    print(target_sum(arr, t))
