"""
Fill in the Tetris Shapes inside an n X m Matrix without Overlap
Shape 1:
[1]

Shape 2:
[1][1][1]

Shape 3:
[1][1]
[1][1]

Shape 4:
[1]
[1][1]
[1]

Shape 5:
   [1]
[1][1][1]

Sample Input: n = 4, m = 4, figures = [4, 2, 1, 3]
Sample Output:
[
[1, 1, 1, 1]
[1, 1, 1, 0]
[1, 1, 1, 0],
[0, 1, 1, 0]
]

Explanation:
Fig[0] = 4    ->   Fig[1] = 2    ->   Fig[1] = 1    ->    Fig[1] = 3
[                 [                  [                   [
[1, 0, 0, 0]      [1, 1, 1, 1]       [1, 1, 1, 1]        [1, 1, 1, 1]
[1, 1, 0, 0]      [1, 1, 0, 0]       [1, 1, 1, 0]        [1, 1, 1, 0]
[1, 0, 0, 0]      [1, 0, 0, 0]       [1, 0, 0, 0]        [1, 1, 1, 0]
[0, 0, 0, 0]      [0, 0, 0, 0]       [0, 0, 0, 0]        [0, 1, 1, 0]
]                 ]                  ]                   ]

"""


def draw_shape_2(new_m, r, c):
    new_m[r][c] = 1
    new_m[r][c + 1] = 1
    new_m[r][c + 2] = 1


def draw_shape_3(new_m, r, c):
    new_m[r][c] = 1
    new_m[r + 1][c] = 1
    new_m[r][c + 1] = 1
    new_m[r + 1][c + 1] = 1


def draw_shape_4(new_m, r, c):
    new_m[r][c] = 1
    new_m[r + 1][c] = 1
    new_m[r + 2][c] = 1
    new_m[r + 1][c + 1] = 1


def draw_shape_5(new_m, r, c):
    new_m[r][c] = 1
    new_m[r + 1][c] = 1
    new_m[r][c + 1] = 1
    new_m[r + 1][c + 1] = 1


def draw_on_mat(new_m, fig):
    n, m = len(new_m), len(new_m[0])

    for i in range(n):
        draw = False
        for j in range(m):
            if new_m[i][j] == 1:
                continue

            if fig == 1 and new_m[i][j] == 0:
                new_m[i][j] = 1
                draw = True
                break
            elif fig == 2 and (new_m[i][j] == 0 and j + 2 < m):
                draw_shape_2(new_m, i, j)
                draw = True
                break
            elif fig == 3 and (new_m[i][j] == 0 and (i + 1 < n and j + 1 < m)):
                draw_shape_3(new_m, i, j)
                draw = True
                break
            elif fig == 4 and new_m[i][j] == 0 and (i + 2 < n and j + 1 < m):
                if new_m[i + 1][j + 1] == 0:
                    draw_shape_4(new_m, i, j)
                    draw = True
                    break
            elif fig == 5 and (new_m[i][j] == 0 and (i + 1 >= 0 and j + 2 < m)):
                if new_m[i - 1][j + 1] == 0:
                    draw_shape_5(new_m, i, j)
                    draw = True
                    break
        if draw:
            break


def solution(n, m, figures):
    new_m = [[0 for _ in range(m)] for _ in range(n)]

    for fig in figures:
        draw_on_mat(new_m, fig)
        for l in range(4):
            print(new_m[l])
        print('\n')

    return new_m


if __name__ == '__main__':
    res = solution(4, 4, [4, 1, 2, 3])
    for i in range(4):
        print(res[i])
