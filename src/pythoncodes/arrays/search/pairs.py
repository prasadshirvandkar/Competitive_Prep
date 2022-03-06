def pairs(arr, k):
    set_arr = set([a for a in arr])
    count = 0
    for a in arr:
        if a + k in set_arr:
            count += 1

    return count


if __name__ == '__main__':
    k_value = 2
    nums = [1, 5, 3, 4, 2]
    print(pairs(nums, k_value))
