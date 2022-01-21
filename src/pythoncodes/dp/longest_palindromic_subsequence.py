def lps(s, i, j):
    if i < 0 or j < 0 or j < i:
        return 0

    if i == j:
        return 1

    if s[i] == s[j]:
        return 2 + lps(s, i + 1, j - 1)

    both = max(lps(s, i + 1, j), lps(s, i, j - 1))
    return both


if __name__ == '__main__':
    st = 'agrbcbra'
    print(lps(st, 0, len(st) - 1))
