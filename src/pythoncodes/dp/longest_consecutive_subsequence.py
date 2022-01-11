def find_lcs():
    s1 = 'bbbab'
    s2 = 'babbb'

    a = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(0, len(s1) + 1):
        for j in range(0, len(s2) + 1):
            if i > 0 and j > 0:
                a[i][j] = 1 + a[i - 1][j - 1] if s1[i - 1] == s2[j - 1] else max(a[i - 1][j], a[i][j - 1])

    print(a[len(s1) - 1][len(s2) - 1])


def find_lps():
    sp1 = 'bbbab'
    sp_l = len(sp1)
    dp = [[0 for _ in range(sp_l)] for _ in range(sp_l)]
    for i in range(0, sp_l):
        for j in range(0, sp_l):
            dp[i][j] = 1 + dp[i - 1][j - 1] if sp1[i] == sp1[sp_l - j - 1] else max(dp[i - 1][j], dp[i][j - 1])

    print(dp)


if __name__ == '__main__':
    find_lcs()
    find_lps()
    