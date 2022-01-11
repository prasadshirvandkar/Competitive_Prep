def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def sort_colors(nums):
    left, right, it = 0, len(nums) - 1, 0
    while it <= right:
        if nums[it] == 0:
            swap(nums, left, it)
            left += 1
            it += 1
        elif nums[it] == 1:
            it += 1
        elif nums[it] == 2:
            swap(nums, it, right)
            right -= 1


if __name__ == '__main__':
    arr = [2, 0, 1]
    sort_colors(arr)
    print(arr)
