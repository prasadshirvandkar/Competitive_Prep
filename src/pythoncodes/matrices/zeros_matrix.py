def set_zero_matrix(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                if i > 0:
                    matrix[i - 1][j] = i - 1 + j + 10
                if i < r - 1:
                    matrix[i + 1][j] = i + 1 + j + 30
                if j > 0:
                    matrix[i][j - 1] = i + j - 1 + 40
                if j < c - 1:
                    matrix[i][j + 1] = i + j + 1 + 20

            if i < r - 1 and matrix[i][j] == i + j + 30:
                matrix[i + 1][j] = i + 1 + j + 30
            if j > 0 and (matrix[i][j] == i + j + 40 and matrix[i][j - 1] != i + j - 1 + 30):
                matrix[i][j - 1] = i + j - 1 + 40
            if j < c - 1 and (matrix[i][j] == i + j + 20 and matrix[i][j + 1] != i + j + 1 + 30):
                matrix[i][j + 1] = i + j + 1 + 20

    for m in matrix:
        print(m)


if __name__ == '__main__':
    mat = [[0, 1, 2, 0], [3, 0, 5, 2], [1, 3, 1, 5]]
    mat1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    set_zero_matrix(mat)
