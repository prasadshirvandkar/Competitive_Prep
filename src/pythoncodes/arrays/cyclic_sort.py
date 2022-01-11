def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        c = nums[i] - 1
        if nums[i] != nums[c]:
            nums[i], nums[c] = nums[c], nums[i]
        else:
            i += 1


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    cyclic_sort(arr)

    print(arr)
