# Find K Closest Elements. TC = O(logn)
def find_k_closest(nums, x, k):
    if len(nums) == k:
        print(nums)

    # Binary Search for Searching Closest Element
    left = 0
    right = len(nums) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > x:
            right = mid - 1
        elif nums[mid] < x:
            left = mid + 1
        else:
            break

    left = mid - 1
    right = mid

    # Keep Expanding Left-Right Window for K Closest Elements
    while right - left - 1 < k:
        if left == -1:
            right += 1
            continue

        if right == len(nums) or abs(nums[left] - x) <= abs(nums[right] - x):
            left -= 1
        else:
            right += 1

    print("Left: " + str(left + 1) + " -> " + "Right: " + str(right))


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k1, x1 = 4, 3
    find_k_closest(arr, k1, x1)

