def find_peak_element(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return nums[mid]
        elif nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return nums[low]


if __name__ == '__main__':
    arr = [1, 2, 3, 1]
    print(find_peak_element(arr))
