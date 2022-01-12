def chessboard_pattern(n):
    board = []

    c1, c2 = 'W', 'B'
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(c2 if j & 1 == 1 else c1)
        c1, c2 = c2, c1
        board.append(temp)

    for b in board:
        print(b)


def chessboard_alt(n):
    s_board = []
    r_board = []

    switch = True
    for i in range(n):
        s_board.append('W' if switch else 'B')
        r_board.append('B' if switch else 'W')
        switch = not switch

    board = [r_board if i & 1 == 1 else s_board for i in range(n)]

    print()
    for b in board:
        print(b)


if __name__ == '__main__':
    blocks = 8
    chessboard_pattern(blocks)
    chessboard_alt(blocks)
