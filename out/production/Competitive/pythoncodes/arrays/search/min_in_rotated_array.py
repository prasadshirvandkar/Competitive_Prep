# Minimum in Rotated Array. TC = O(logn)
def min_in_rotated(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    print(nums[left])
    print(left)


if __name__ == '__main__':
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [15, 19, 20, 25, 26, 1, 3, 5, 8, 10, 12, 14]
    min_in_rotated(arr)



