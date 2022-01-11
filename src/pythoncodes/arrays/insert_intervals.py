def insert_interval(intervals, newInterval):
    merged_intervals = []

    if len(intervals) == 0:
        return [newInterval]

    for i in intervals:
        if newInterval[0] > i[1]:
            merged_intervals.append(i)
        if newInterval[1] < i[0]:
            merged_intervals.append(newInterval)
            newInterval = i
        else:
            newInterval = [min(newInterval[0], i[0]), max(newInterval[1], i[1])]

    merged_intervals.append(newInterval)
    return merged_intervals


if __name__ == '__main__':
    arr = [[1, 3], [6, 9]]
    arr1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    arr2 = [[0, 5]]
    arr3 = [[1, 2], [4, 17], [6, 7], [8, 10], [12, 16]]
    interval = [4, 8]
    print(insert_interval(arr1, interval))
