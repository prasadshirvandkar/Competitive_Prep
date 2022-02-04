"""
You are given a matrix of integers matrix of size n × m and a list of queries.
The given matrix is colored in black and white in a checkerboard style - the top left corner is colored white and any
two side-neighboring cells have opposite colors.
Example

For

matrix = [[2, 0, 4],
          [2, 8, 5],
          [6, 0, 9],
          [2, 7, 10],
          [4, 3, 4]]
and queries = [[0, 0], [1, 3]], the output should be

meanAndChessboard(matrix, queries) = [[1, 2, 4],
                                      [2, 8, 5],
                                      [6, 0, 9],
                                      [2, 7, 10],
                                      [4, 3, 3]]
The average of the 0th black cell and the 0th white cell is (0 + 2) / 2 = 1, so both cells are replaced with 1.
The average of the 1st black cell and the 3rd white cell is (1 + 4) / 2 = 2.5, so the 1 is replaced with floor(2.5) = 2
and the 4 is replaced with ceil(2.5) = 3.
"""

# One of the worst written code, I have ever written but too lazy to make it clean now

import math


def checkboard_mat(mat, query):
    whites, blacks = [], []
    nr, nc = len(mat), len(mat[0])

    for i in range(nr):
        for j in range(nc):
            if i % 2 == 0:
                if j % 2 == 0:
                    whites.append([mat[i][j], (i, j)])
                else:
                    blacks.append([mat[i][j], (i, j)])
            else:
                if j % 2 == 0:
                    blacks.append([mat[i][j], (i, j)])
                else:
                    whites.append([mat[i][j], (i, j)])

    for q in query:
        whites.sort()
        blacks.sort()
        b = blacks[q[0]]
        w = whites[q[1]]
        avg = (b[0] + w[0]) / 2
        if avg.is_integer():
            blacks[q[0]] = [int(avg), b[1]]
            whites[q[1]] = [int(avg), w[1]]
        else:
            blacks[q[0]] = [math.floor(avg), b[1]]
            whites[q[1]] = [math.ceil(avg), w[1]]

    for w in whites:
        loc = w[1]
        mat[loc[0]][loc[1]] = w[0]

    for b in blacks:
        loc = b[1]
        mat[loc[0]][loc[1]] = b[0]

    return mat


if __name__ == '__main__':
    matrix = [
        [1, 9, 10, 8],
        [3, 4, 4, 4]
    ]

    queries = [[2, 3], [3, 2]]
    print(checkboard_mat(matrix, queries))

    matrix1 = [
        [2, 0, 4],
        [2, 8, 5],
        [6, 0, 9],
        [2, 7, 10],
        [4, 3, 4]
    ]

    queries1 = [[0, 0], [1, 3]]
    print(checkboard_mat(matrix1, queries1))
