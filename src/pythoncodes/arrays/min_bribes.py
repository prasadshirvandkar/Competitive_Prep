def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print(f"{q[i]} => {i + 1}")
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            print(f"{q[i]} => {q[j]}")
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    arr = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(arr)
    arr1 = [2, 5, 1, 3, 4]
    minimumBribes(arr1)
