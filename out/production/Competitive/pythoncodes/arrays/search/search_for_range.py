def search_for_range(nums, target):
    if len(nums) == 0:
        return [-1, -1]

    n = len(nums) - 1
    low, high = 0, n
    start, end = -1, -1
    while low <= high:
        mid = (low + high) // 2
        if start == -1:
            if (mid - 1 >= 0 and nums[mid] == target and nums[mid - 1] < nums[mid]) \
                    or (mid == 0 and nums[mid] == target):
                start = mid
                low = mid
                high = n
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if (mid + 1 <= n and nums[mid] == target and nums[mid + 1] > target) \
                    or (mid == n and nums[mid] == target):
                end = mid
                break
            elif nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

    return start, end


if __name__ == '__main__':
    arr = [5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 10, 10, 10]
    t = 7
    arr1 = [5, 7, 7, 8, 8, 10, 10]
    arr2 = [5, 6, 7, 8, 9, 10]
    arr3 = []
    print(search_for_range(arr, t))
