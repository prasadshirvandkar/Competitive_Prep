def plus_one(nums):
    carry = False
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 9:
            nums[i] = 0
            if i == 0:
                carry = True
        else:
            nums[i] += 1
            break

    if carry:
        nums.insert(0, 1)

    return nums


if __name__ == '__main__':
    print(plus_one([1, 9, 9, 9]))
