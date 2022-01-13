def find_palindrome_substring_window(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def longest_palindrome_substring(s):
    n = len(s)
    if s is None or n == 1:
        return 0

    max_len = 0
    for i in range(0, n):
        # Expand window for single letter palindrome like bab
        len1 = find_palindrome_substring_window(s, i, i)
        # Expand window for double letter palindrome like baab
        len2 = find_palindrome_substring_window(s, i, i + 1)
        m_len = max(len1, len2)
        max_len = max(max_len, (i + (m_len // 2) - (i - ((m_len - 1) // 2))) + 1)

    return max_len


if __name__ == '__main__':
    st = 'baabad'
    print(longest_palindrome_substring(st))
