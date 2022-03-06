def check_palindrome(s):
    is_palin = True
    for i in range(len(s) // 2):
        if s[0] != s[len(s) - i - 1]:
            is_palin = False
    return is_palin


def print_substrings(s, start, idx, temp):
    for i in range(idx, len(s) + 1):
        sub_st = s[start: i]
        print(f"{start} -> {i}")
        if len(sub_st) > 1 and check_palindrome(sub_st):
            temp.append(sub_st)
        print_substrings(s, start, i + 1, temp)
        print("Back " + str(i))
        start += 1
    return 0


def special_string(s):
    res = []
    print_substrings(s, 0, 1, res)
    print(res)
    return len(s) + len(res)


if __name__ == '__main__':
    st = 'asasd'
    print(special_string(st))
