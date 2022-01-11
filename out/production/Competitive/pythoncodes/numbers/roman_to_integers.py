def roman_to_int(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_int = roman_dict[s[len(s) - 1]]
    for i in range(len(s) - 2, - 1, -1):
        roman_int += roman_dict[s[i]] if roman_dict[s[i]] >= roman_dict[s[i + 1]] else -roman_dict[s[i]]

    return roman_int


if __name__ == '__main__':
    print(roman_to_int('CM'))
