"""
Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many
ways exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the
removal. Note that we are removing only a single instance of a single digit, rather than all instances (eg: removing 1
from the string a11b1c could result in a1b1c or a11bc, but not abc).
"""


def lex_string(s, t):
    i, j = 0, 0
    count = 0
    while i < len(s) and j < len(t):
        if s[i].isdigit():
            new_st = s[0:i] + s[i + 1:]
            if new_st < t:
                count += 1
        i += 1

        if t[j].isdigit():
            new_tt = t[0:j] + t[j + 1:]
            if new_tt > s:
                count += 1
        j += 1

    return count


if __name__ == '__main__':
    st = '6'
    tt = 'h'

    print(lex_string(st, tt))
