"""
It was based on elimination of round wise maximum elements from a 2D matrix.

7 1 2          1 2              1

2 4 6   ->    2 4     ->     2      ->      [ 7 + 4 + 2] = 13

3 1 2          1 2              1
"""


def round_wise_max(mat):
    rw_dict = {}

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j in rw_dict:
                rw_dict[j].append(mat[i][j])
            else:
                rw_dict[j] = [mat[i][j]]

    print(rw_dict)
    max_count = 0
    for k, v in rw_dict.items():
        max_count += max(v)
    return max_count


if __name__ == '__main__':
    matrix = [
        [7, 1, 2],
        [2, 4, 6],
        [3, 1, 2]
    ]

    print(round_wise_max(matrix))
