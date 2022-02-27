def backspace_compare(s, t):
    b_count = 0
    s1_s, s2_s = '', ''

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '#':
            b_count += 1
        elif b_count > 0:
            b_count -= 1
        else:
            s1_s += s[i]

    b_count = 0
    for i in range(len(t) - 1, -1, -1):
        if t[i] == '#':
            b_count += 1
        elif b_count > 0:
            b_count -= 1
        else:
            s2_s += t[i]

    return s1_s == s2_s


if __name__ == '__main__':
    s1 = 'ab#c'
    s2 = 'ad#c'
    print(backspace_compare(s1, s2))
