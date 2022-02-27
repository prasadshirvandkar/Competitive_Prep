def ways_to_split_string(st):
    l_prefix, r_prefix = [0 for _ in range(len(st))], [0 for _ in range(len(st))]

    alpha_set = set()
    for i in range(0, len(st)):
        if st[i] in alpha_set:
            l_prefix += 1
        else:
             alpha_set.add(st[i])

    for i in range(0, len(st)):
        if st[i] in alpha_set:
            l_prefix += 1
        else:
            alpha_set.add(st[i])

    return 0


if __name__ == '__main__':
    s = 'aacaba'
    print(ways_to_split_string(s))
