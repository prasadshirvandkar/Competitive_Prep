def generate_combinations(s, k, temp, results):
    for j in range(len(s)):
        temp.append(s[j])
        if len(temp) == k:
            results.append(''.join(temp))
        else:
            generate_combinations(s, k, temp, results)
        temp.pop(-1)

    return results


def k_letter_combinations(s, k):
    if len(s) == 0:
        return []
    return generate_combinations(s, k, [], [])


if __name__ == '__main__':
    st = ['a', 'b']
    length = 4
    print(k_letter_combinations(st, length))
