def reverse(arr, i):
    if i == len(arr) // 2:
        return

    reverse(arr, i + 1)
    arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]


def print_subsequences(arr, l, r):
    if l <= r:
        print(arr[l:r])

    for i in range(l, r):
        print_subsequences(arr, l + 1, i)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    reverse(nums, 0)
    print(nums)

    nums1 = [3, 1, 2]
    print_subsequences(nums1, 0, len(nums) - 1)
