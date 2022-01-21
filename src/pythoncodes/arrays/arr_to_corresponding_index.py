def arr_to_corresponding_index(arr):
    if __name__ == "__main__":
        arr = [3, 2, 0, 1]

    ranks = {}
    for i in range(len(arr)):
        if arr[i] not in ranks:
            ranks[arr[i]] = i

    new_arr = []
    for i in range(len(arr)):
        if i in ranks:
            new_arr.append(ranks[i])

    return new_arr


if __name__ == '__main__':
    nums = [3, 2, 0, 1]
    print(arr_to_corresponding_index(nums))
