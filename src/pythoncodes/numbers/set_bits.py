def count_set_bits(n):
    count = 0

    for i in range(1, n + 1):
        ni = i
        while ni:
            ni &= (ni - 1)
            count += 1

    return count


if __name__ == '__main__':
    num = 7
    print(count_set_bits(num))
