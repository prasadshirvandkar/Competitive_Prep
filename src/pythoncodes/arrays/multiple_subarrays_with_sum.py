def multiple_subarray_with_given_sum(nums, sumN):
    trackMap = {0: [-1]}
    currSum = 0

    for i in range(0, len(nums)):
        currSum += nums[i]

        temp = currSum - sumN
        if temp in trackMap:
            for j in trackMap[temp]:
                print(str(j + 1) + " -> " + str(i))
            trackMap[temp].append(i)
        else:
            trackMap[currSum] = [i]

    for p, m in trackMap.items():
        print(str(p) + " -> " + str(m))


if __name__ == '__main__':
    arr = [3, 4, -7, 1, 3, 3, 1, -4]
    s = 7
    multiple_subarray_with_given_sum(arr, s)
