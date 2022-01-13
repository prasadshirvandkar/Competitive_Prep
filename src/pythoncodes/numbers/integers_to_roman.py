# Try Some Other Day

def int_to_roman(num):
    roman_dict = {
        0: '',
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    numbers = []
    prod = 1
    while num > 0:
        numbers.append((num % 10) * prod)
        num //= 10
        if num <= 0:
            break
        prod *= 10

    roman = ''
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] not in roman_dict:
            if 5 <= numbers[i] <= 8:
                roman += 'V'
                for j in range(numbers[i] - 5):
                    roman += 'I'
            elif 50 <= numbers[i] <= 99:
                roman += 'L'
            else:
                count = numbers[i] // prod
                for j in range(count):
                    roman += roman_dict[numbers[i] // count]
        else:
            roman += roman_dict[numbers[i]]
        prod //= 10

    return roman

# "MDLXVII"


if __name__ == '__main__':
    n = 78
    print(int_to_roman(n))
