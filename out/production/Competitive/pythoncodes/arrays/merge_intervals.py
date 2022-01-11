def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []

    a, b = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        if b < intervals[i][0]:
            merged_intervals.append([a, b])
            a = intervals[i][0]
        b = max(b, intervals[i][1])

    merged_intervals.append([a, b])

    return merged_intervals


if __name__ == '__main__':
    arr = [[1, 4], [4, 5]]
    arr1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    arr2 = [[1, 3], [2, 6], [8, 16], [15, 18]]
    arr3 = [[1, 4], [2, 3], [3, 4], [4, 5], [5, 6], [8, 10], [11, 13]]
    arr4 = [[1, 4], [2, 3], [3, 13], [4, 5], [5, 6], [8, 10], [11, 13]]
    print(merge_intervals(arr3))
