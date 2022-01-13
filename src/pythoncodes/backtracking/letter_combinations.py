digit_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def generate_combinations(digits, i, n, temp, results):
    letters = digit_map[digits[i]]
    for d in range(len(letters)):
        temp.append(letters[d])
        if len(temp) == n:
            results.append(''.join(temp))
        else:
            generate_combinations(digits, i + 1, n, temp, results)
        temp.pop(-1)

    return results


def letter_combinations(digits):
    if len(digits) == 0:
        return []

    return generate_combinations(digits, 0, len(digits), [], [])


if __name__ == '__main__':
    digit = '237'
    print(letter_combinations(digit))
