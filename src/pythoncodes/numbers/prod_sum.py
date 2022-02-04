def prod_sum(n):
    prod = 1
    sm = 0

    while n > 0:
        temp = n % 10
        prod *= temp
        sm += temp
        n //= 10

    return prod - sm


if __name__ == '__main__':
    num = 12345
    print(prod_sum(num))
