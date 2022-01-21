def n_candy_distribution(n):
    distribution = [1 for _ in range(len(n))]

    for i in range(1, len(n)):
        if n[i] > n[i - 1]:
            distribution[i] = distribution[i - 1] + 1

    sum = 0
    for i in range(0, len(n) - 1):
        distribution[i] = max(distribution[i], distribution[i + 1] + 1)
        sum += max(distribution[i], distribution[i + 1] + 1)

    print(distribution)
    print(sum)
    return 0


if __name__ == '__main__':
    candies = [1, 5, 2, 1]

    print(n_candy_distribution(candies))
