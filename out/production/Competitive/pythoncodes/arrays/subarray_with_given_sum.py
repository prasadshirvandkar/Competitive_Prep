def find_subarray_with_given_sum(nums, sumN):
    start = 0
    end = 0
    tempSum = 0
    for i in range(0, len(nums)):
        tempSum += nums[i]
        end += 1
        if 0 < sumN <= tempSum:
            break
        elif 0 > sumN >= tempSum:
            break

    while tempSum > sumN and start < len(nums):
        tempSum -= nums[start]
        start += 1

    print(str(start) + " -> " + str(end - 1))


if __name__ == '__main__':
    arr = [10, 2, -2, -20, 10]
    s = 10
    find_subarray_with_given_sum(arr, s)
