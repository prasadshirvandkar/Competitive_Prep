"""
Given an m*n 2d matrix, filled with pos numbers. Place 2 roosters on the matrix, and they cannot be in the same row or col.
The value is the total sum EXCEPT rows/columns that rooster is placed. Find the maximum value after placing 2 roosters.
Example:
"X" denoted as rooster
1 X 3
X 5 6
7 8 9

The value is 5+6+8+9
"""


def calc(mat, rc):
    sm = 0
    for j in range(len(mat)):
        if j != rc[0]:
            for k in range(len(mat[0])):
                if k != rc[1]:
                    sm += mat[j][k]
    return sm


def backtrack_mat(mat, rc, max_sum):
    for i in range(len(mat[0])):
        rc.append(i)
        max_sum = max(max_sum, calc(mat, rc)) if len(rc) == 2 else backtrack_mat(mat, rc, max_sum)
        rc.pop(-1)

    return max_sum


def rooster_matrix(mat):
    return backtrack_mat(mat, [], -1)


if __name__ == '__main__':
    matrix = [[1, 10, 11], [4, 5, 6], [7, 8, 9]]
    print(rooster_matrix(matrix))
