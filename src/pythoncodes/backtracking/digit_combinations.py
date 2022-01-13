def generate_combinations(n, k, s, temp, results):
    for i in range(s, n + 1):
        temp.append(i)
        if len(temp) == k:
            results.append([i for i in temp])
        else:
            generate_combinations(n, k, i + 1, temp, results)
        temp.pop(-1)
    return results


def digit_combinations(n, k):
    if n == 1:
        return [[1]]
    return generate_combinations(n, k, 1, [], [])


if __name__ == '__main__':
    num = 4
    length = 2
    print(digit_combinations(num, length))
