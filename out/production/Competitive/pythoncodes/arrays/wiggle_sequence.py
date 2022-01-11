def wiggle_max_length(nums) -> int:
    n = len(nums)
    if n <= 1:
        return n
    count = 1
    i = 1
    while i < n and nums[i] == nums[i - 1]:
        i += 1
    if i == n:
        return count
    prev = nums[i] - nums[i - 1]
    while i < n:
        if nums[i] == nums[i - 1]:
            i += 1
            continue
        else:
            curr = nums[i] - nums[i - 1]
            if curr * prev < 0:
                count += 1
                prev = curr
            i += 1
            continue
    return count + 1


if __name__ == "__main__":
    arr = [33, 53, 12, 64, 50, 41, 45, 21, 97, 35, 47, 92, 39, 0, 93, 55, 40, 46, 69, 42, 6, 95, 51, 68, 72, 9, 32, 84,
           34, 64, 6, 2, 26, 98, 3, 43, 30, 60, 3, 68, 82, 9, 97, 19, 27, 98, 99, 4, 30, 96, 37, 9, 78, 43, 64, 4, 65,
           30, 84, 90, 87, 64, 18, 50, 60, 1, 40, 32, 48, 50, 76, 100, 57, 29, 63, 53, 46, 57, 93, 98, 42, 80, 82, 9,
           41, 55, 69, 84, 82, 79, 30, 79, 18, 97, 67, 23, 52, 38, 74, 15]

    count = 1
    up = -1
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i] and up != 1:
            count += 1
            up = 1
        elif arr[i - 1] > arr[i] and up != 0:
            count += 1
            up = 0

    print(count)
    print(wiggle_max_length(arr))
