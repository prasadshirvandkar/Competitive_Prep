def one_d_to_two_d_array(original, m, n):
    if m * n != len(original):
        return []

    two_d_arr = []
    temp = []
    for i in range(len(original)):
        if len(temp) > 0 and len(temp) % n == 0:
            two_d_arr.append(temp)
            temp = []
        temp.append(original[i])

    if len(temp) > 0 and len(temp) % n == 0:
        two_d_arr.append(temp)

    return two_d_arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(one_d_to_two_d_array(arr, 6, 2))
