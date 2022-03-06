def swap(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]


def permutations(s, idx, N):
    if idx == N:
        print(s)
        return

    for i in range(idx, N):
        s[idx], s[i] = s[i], s[idx]
        permutations(s, idx + 1, N)
        s[idx], s[i] = s[i], s[idx]


if __name__ == '__main__':
    string = "1234"
    permutations([c for c in string], 0, len(string))
