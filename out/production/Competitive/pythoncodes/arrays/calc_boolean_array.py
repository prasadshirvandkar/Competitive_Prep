if __name__ == "__main__":
    arr = [8, 5, 6, 16, 5]
    l, r = 1, 3

    b_arr = [False for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(l, r):
            if (i + 1) * j == arr[i]:
                b_arr[i] = True
                break

    print(b_arr)