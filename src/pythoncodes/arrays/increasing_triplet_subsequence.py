def increasing_triplet_subseq(nums):
    count = 1
    start = 1

    curr = nums[0]
    while count < 3 and start < len(nums):
        if nums[start] < curr:
            curr = nums[start]
        elif nums[start] > curr:
            count += 1
            curr = nums[start]
        else:
            start += 1

    return count == 3


if __name__ == '__main__':
    arr = [5, 4, 7, 1, 6]
    arr1 = [20, 100, 10, 12, 5, 13]
    print(increasing_triplet_subseq(arr1))
