def find_sum_subarray_of_size_k(nums, k):
    left, right = 0, 0

    temp = nums[left]
    max_len = 0
    while left <= right < len(nums):
        if temp == k:
            max_len = max(max_len, (right - left) + 1)
            temp -= nums[left]
            left += 1
            right += 1
            temp += nums[right]
        elif temp < k:
            right += 1
            if right < len(nums):
                temp += nums[right]
        else:
            temp -= nums[left]
            left += 1

    return max_len


if __name__ == '__main__':
    arr = [4, 1, 1, 1, 2, 2, 5]
    sm = 6

    print(find_sum_subarray_of_size_k(arr, sm))
