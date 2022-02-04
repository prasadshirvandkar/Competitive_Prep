def valid_palindrome(s):
    i, j = 0, len(s) - 1
    s = s.lower()
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        elif not (s[i].isalpha() or s[i].isdigit()):
            i += 1
        elif not (s[j].isalpha() or s[j].isdigit()):
            j -= 1
        else:
            return False

    return True


if __name__ == '__main__':
    st2 = '0P'
    print(valid_palindrome(st2))
