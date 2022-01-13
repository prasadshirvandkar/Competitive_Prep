def is_valid(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < len(board[0]):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def n_queen_backtracking(board, row, count):
    for c in range(len(board[0])):
        if is_valid(board, row, c):
            board[row][c] = 1
            if row + 1 == len(board):
                count += 1
            else:
                count = n_queen_backtracking(board, row + 1, count)
            board[row][c] = 0

    return count


if __name__ == '__main__':
    mat = [[0 for _ in range(4)] for _ in range(4)]
    print(n_queen_backtracking(mat, 0, 0))
