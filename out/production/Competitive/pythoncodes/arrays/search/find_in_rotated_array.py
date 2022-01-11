# Rotated Array Search. TC = O(logn)
def find_in_rotated_array(nums, target):
    low = 0
    high = len(nums) - 1
    found = -1

    first = nums[low]
    last = nums[high]

    while low <= high:
        mid = (low + high) // 2
        midValue = nums[mid]
        if midValue == target:
            found = mid
            break
        elif midValue >= last >= target:
            if midValue > target:
                low = mid + 1
            else:
                high = mid - 1
        elif midValue <= first <= target:
            high = mid - 1
        else:
            if midValue < target:
                low = mid + 1
            else:
                high = mid - 1

    print(found)


if __name__ == '__main__':
    arr = [1, 3]
    t = 3
    find_in_rotated_array(arr, t)
