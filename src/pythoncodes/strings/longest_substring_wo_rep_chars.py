def longest_substring_without_repeating_chars(s):
    best = 0
    freq = {}
    j = 0

    for i in range(len(s)):
        print(freq)
        if s[i] in freq:
            j = max(freq[s[i]] + 1, j)
        freq[s[i]] = i
        if i - j + 1 > best:
            best = i - j + 1
            print(str(j) + ' -> ' + str(i))

    return best


if __name__ == '__main__':
    st = 'abracadabar'
    print(longest_substring_without_repeating_chars(st))
