def duplicates_in_array(nums):
    i = 0
    dups = set()

    while i < len(nums):
        c = nums[i] - 1
        if nums[i] != nums[c]:
            nums[i], nums[c] = nums[c], nums[i]
        else:
            if nums[i] == nums[c] and c != i:
                dups.add(nums[i])
            i += 1

    return list(dups)


if __name__ == '__main__':
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(duplicates_in_array(arr))
