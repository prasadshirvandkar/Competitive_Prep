def house_robber(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    max_till = max(nums[0], nums[1])

    if len(nums) == 2:
        return max_till
    else:
        nums[1] = max_till
        for i in range(2, len(nums)):
            max_till = max(nums[i - 2] + nums[i], max_till)
            nums[i] = max_till

    return max_till


def house_robber_rec(nums, i):
    if i == 0:
        return nums[i]

    if i < 0:
        return 0

    pick = nums[i] + house_robber_rec(nums, i - 2)
    not_pick = 0 + house_robber_rec(nums, i - 1)

    return max(pick, not_pick)


if __name__ == '__main__':
    arr = [2, 7, 9, 3, 1]
    arr1 = [1, 11, 1, 1, 10]
    arr2 = [2, 1, 1, 2]
    print(house_robber(arr1))
    print(house_robber_rec(arr1, len(arr1) - 1))
