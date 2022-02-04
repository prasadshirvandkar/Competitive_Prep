def backtrack(arr, query, start, j, count):
    if j == len(query):
        count += 1
        return count

    for i in range(start, len(arr)):
        if arr[i] == query[j] and j < len(query):
            count = backtrack(arr, query, i + 1, j + 1, count)

    return count


def occurring_subsequence(queries, arr):
    return [backtrack(arr, query, 0, 0, 0) for query in queries]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    q = [
        [1, 2, 3],
        [2, 4, 3],
        [1, 1, 1]
    ]

    a1 = [1, 2, 2, 1, 2, 1, 2]
    q1 = [[1, 1, 2], [1, 2, 1]]

    print(occurring_subsequence(q1, a1))
