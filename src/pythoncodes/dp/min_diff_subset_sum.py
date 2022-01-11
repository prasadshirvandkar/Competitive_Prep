def min_diff_subset_sum(nums):
    n = len(nums)
    sm = sum(nums)
    dp = [[0 for _ in range(sm + 1)] for _ in range(1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        i_dp = []
        for j in range(0, sm + 1):
            if j == 0:
                i_dp.append(1)
            elif j < nums[i - 1]:
                i_dp.append(dp[i - 1][j])
            else:
                i_dp.append(dp[i - 1][j] or dp[i - 1][j - nums[i - 1]])
        dp.append(i_dp)

    mini = sm
    for i in range(len(dp[-1]) // 2):
        if dp[-1][i] == 1:
            mini = min(sm - i, mini)

    return mini - (sm - mini)


if __name__ == '__main__':
    s = [1, 2, 7]
    print(min_diff_subset_sum(s))
