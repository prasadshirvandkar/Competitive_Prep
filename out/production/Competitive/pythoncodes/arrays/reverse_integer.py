def swap(s, i, j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp


def reverse_integer(x):
    x = str(x)
    minus = x[0] == '-'
    zero = x[len(x) - 1] == '0'
    s = 1 if minus else 0
    e = len(x) - 1 if zero else len(x)
    x = x[s:e][::-1]
    x = int(f"-{x}") if minus else int(x)

    return 


if __name__ == '__main__':
    n = 0
    print(reverse_integer(n))
