def valid_sudoku(board):
    rows, cols, blocks = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
    row_num = -3
    for i in range(len(board)):
        if i % 3 == 0:
            row_num += 3
        col_num = row_num - 1
        for j in range(len(board[0])):
            if j % 3 == 0:
                col_num += 1

            if board[i][j] != '.' and (
                    board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in blocks[col_num]):
                return False

            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            blocks[col_num].add(board[i][j])

    return True


if __name__ == '__main__':
    b = [
        ["7", ".", ".", ".", "4", ".", ".", ".", "."],
        [".", ".", ".", "8", "6", "5", ".", ".", "."],
        [".", "1", ".", "2", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "9", ".", ".", "."],
        [".", ".", ".", ".", "5", ".", "5", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    asd = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]

    print(valid_sudoku(b))
