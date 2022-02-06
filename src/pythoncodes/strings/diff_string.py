def diff_string(strs):
    invalid = []
    for st in strs:
        if len(st) >= 2:
            diff = ord(st[1]) - ord(st[0])
            for i in range(2, len(st)):
                if ord(st[i]) - ord(st[i - 1]) != diff:
                    invalid.append(st)
                    break

    return invalid


if __name__ == '__main__':
    s = ["ABC", "BCD", "DEG", "ACE"]
    print(diff_string(s))
