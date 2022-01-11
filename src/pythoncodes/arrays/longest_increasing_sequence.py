def lis(nums):
    if len(nums) == 0:
        return 0

    nums_set = set([n for n in nums])

    max_lis = 0
    for i in range(len(nums)):
        if nums[i] - 1 not in nums_set:
            n = nums[i]
            count = 0
            while n in nums_set:
                n += 1
                count += 1
            max_lis = max(count, max_lis)

    return max_lis


if __name__ == '__main__':
    arr = [100, 4, 200, 1, 3, 2]
    arr1 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(lis(arr1))

