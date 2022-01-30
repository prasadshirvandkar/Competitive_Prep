def swap(s, i, j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp


def next_permutation(nums):
    n = len(nums)
    mIndex = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            mIndex = i
            sm = n - 1
            while nums[mIndex] >= nums[sm]:
                sm -= 1
            swap(nums, mIndex, sm)
            print(nums)
            break

    for i in range(mIndex + 1, (n + mIndex + 1) // 2):
        swap(nums, i, n + mIndex - i)


if __name__ == '__main__':
    arr = [1, 3, 2, 4, 3]
    next_permutation(arr)

    print(arr)
