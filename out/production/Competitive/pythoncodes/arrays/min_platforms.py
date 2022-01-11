def min_platforms_needed_for_trains(arr, dep):
    arr = [int(ar) for ar in arr]
    dep = [int(dp) for dp in dep]

    arr.sort()
    dep.sort()

    i, j = 0, 1
    platforms_needed = -1
    p = 1
    while i < len(arr) and j < len(dep):
        if arr[j] > dep[i]:
            i += 1
            p -= 1
        else:
            j += 1
            p += 1

        platforms_needed = max(platforms_needed, p)

    return platforms_needed


if __name__ == '__main__':
    a = ['0900', '0940', '0950', '1100', '1500', '1800']
    d = ['0910', '1200', '1120', '1130', '1900', '2000']

    a1 = ['0900', '1100', '1135']
    d1 = ['1000', '1200', '1240']

    min_platforms_needed_for_trains(a1, d1)
