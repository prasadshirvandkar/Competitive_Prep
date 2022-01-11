def count_and_say(n):
    if n == 1:
        return "1"

    if n == 2:
        return "11"

    s = "11"
    for i in range(3, n + 1):
        c = 0
        temp = ""
        for j in range(0, len(s)):
            c += 1
            if j + 1 >= len(s) or s[j] != s[j + 1]:
                temp += str(c) + s[j]
                c = 0

        s = temp

    return s


if __name__ == '__main__':
    count = 10
    print(count_and_say(count))
