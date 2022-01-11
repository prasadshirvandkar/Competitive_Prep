def kth_factor_of_n(n, k):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
            if c == k:
                return i

    return -1


if __name__ == '__main__':
    print(kth_factor_of_n(12, 3))
