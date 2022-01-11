def strangeGrid(h, w) -> list:
    lis = [[''] * w for _ in range(h)]
    c = chr(ord('A') - 1)
    for i in range(w):
        for j in range(h):
            c = chr(ord(c) + 1)
            lis[h - j - 1 if i & 1 == 1 else j][i] = c
    return lis


if __name__ == '__main__':
    mat = strangeGrid(10, 12)
    for m in mat:
        print(m)
