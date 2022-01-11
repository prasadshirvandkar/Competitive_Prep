def prod_array_except_itself(nums):
    p = 1

    res = []
    for n in nums:
        p *= n
        res.append(p)

    p = 1
    for i in range(len(nums) - 1, 0, -1):
        res[i] = res[i - 1] * p
        p *= nums[i]

    res[0] = p
    print(res)


if __name__ == '__main__':
    arr = [4, 3, 2, 1, 2]
    prod_array_except_itself(arr)
