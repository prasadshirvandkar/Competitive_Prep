def minimize_dissatisfaction(times, factor):
    combined = [tuple((times[i], factor[i], (times[i] / factor[i]))) for i in range(len(times))]

    combined.sort(key=lambda t: t[2])

    cs, dissatisfaction = 0, 0
    for i in range(0, len(combined)):
        cs += combined[i][0]
        dissatisfaction += (cs * combined[i][1])

    print(dissatisfaction)


if __name__ == '__main__':
    minimize_dissatisfaction([2, 1, 3], [4, 1, 9])
    minimize_dissatisfaction([1, 3], [10, 2])
    minimize_dissatisfaction([1, 1, 1], [4, 1, 3])
    minimize_dissatisfaction([1, 3, 2], [10, 10, 10])
    minimize_dissatisfaction([1, 3, 4], [2, 10, 2])