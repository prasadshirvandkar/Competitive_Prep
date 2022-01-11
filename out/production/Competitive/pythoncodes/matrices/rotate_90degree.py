def swap(m, i1, j1, i2, j2):
    temp = m[i1][j1]
    m[i1][j1] = m[i2][j2]
    m[i2][j2] = temp


def rotate_by_90_degrees(matrix):
    r, c = len(matrix), len(matrix[0])
    for i in range(0, r):
        for j in range(0, c // 2):
            swap(matrix, i, j, i, c - j - 1)

    for i in range(0, r):
        for j in range(0, c - i):
            swap(matrix, i, j, r - j - 1, c - i - 1)


if __name__ == '__main__':
    mat = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate_by_90_degrees(mat)
    print(mat)
