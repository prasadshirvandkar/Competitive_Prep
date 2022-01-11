def max_sum_subarray(nums):
    res = nums[0]
    sub_sum = 0
    for n in nums:
        sub_sum += n
        res = max(res, sub_sum)
        if sub_sum < 0:
            sub_sum = 0
    return res


if __name__ == '__main__':
    arr = [-1, -2, -3, -4, -5]
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr2 = [5, 4, -1, 7, 8]
    print(max_sum_subarray(arr))
