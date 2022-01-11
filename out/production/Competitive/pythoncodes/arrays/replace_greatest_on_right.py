# Replace Elements with Greatest Element on Right Side
def replace_greatest_on_right(nums):
    n = len(nums)
    max_num = nums[n - 1]

    for i in range(n - 2, -1, -1):
        temp = nums[i]
        nums[i] = max_num
        max_num = max(temp, max_num)

    nums[n - 1] = -1
    print(nums)


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    replace_greatest_on_right(arr)


