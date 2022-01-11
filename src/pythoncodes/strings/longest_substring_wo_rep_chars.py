def longest_substring_without_repeating_chars(s):
    best = 0
    freq = {}
    j = 0

    for i in range(len(s)):
        if s[i] in freq:
            j = max(freq[s[i]] + 1, j)
        freq[s[i]] = i
        best = max(best, i - j + 1)

    return best


if __name__ == '__main__':
    st = 'pwwkew'
    print(longest_substring_without_repeating_chars(st))
