def frog_jumps(nums):
    dp = [0 for _ in range(len(nums) + 1)]
    dp[1] = nums[1] - nums[0]

    for i in range(2, len(nums)):
        dp[i] = min(dp[i - 1] + abs(nums[i - 1] - nums[i]), dp[i - 2] + abs(nums[i - 2] - nums[i]))

    return dp[len(nums) - 1]


def frog_recursion(nums, i):
    if i < 0:
        return 0

    one_step = frog_recursion(nums, i - 1) + abs(nums[i] - nums[i - 1])
    two_step = frog_recursion(nums, i - 2) + abs(nums[i] - nums[i - 2])

    return min(one_step, two_step)


if __name__ == '__main__':
    arr = [10, 20, 30, 10]
    print(frog_jumps(arr))
    print(frog_recursion(arr, len(arr) - 1))
