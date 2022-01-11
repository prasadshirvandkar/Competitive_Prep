import heapq


def kth_largest(nums, k):
    heapq.heapify(nums)
    largest = heapq.nlargest(k, nums)
    return largest[-1]


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 6, 4]
    top = 5

    print(kth_largest(arr, top))
