import heapq


def top_k_frequent(nums, k):
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    h = []
    for key, value in freq.items():
        heapq.heappush(h, (value, key))

    largest = []
    for n in heapq.nlargest(2, h):
        largest.append(n[1])

    return largest


if __name__ == '__main__':
    arr = [1, 2, 1, 2, 1, 3]
    top = 2

    print(top_k_frequent(arr, top))