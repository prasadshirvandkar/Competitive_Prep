from collections import defaultdict


def have_same_frequency(freq: defaultdict, k: int):
    return all([freq[i] == k or freq[i] == 0 for i in freq])


def count_substrings(s: str, k: int) -> int:
    count = 0
    distinct = len(set([i for i in s]))
    for length in range(1, distinct + 1):
        window_length = length * k
        freq = defaultdict(int)
        window_start = 0
        window_end = window_start + window_length - 1
        for i in range(window_start, min(window_end + 1, len(s))):
            freq[s[i]] += 1
        while window_end < len(s):
            if have_same_frequency(freq, k):
                count += 1
            freq[s[window_start]] -= 1
            window_start += 1
            window_end += 1
            if window_end < len(s):
                freq[s[window_end]] += 1
    return count


def count_substrings_alt(st, k):
    i = 0
    j = 0
    count = 0
    freq = {'a': 1, 'b': 0, 'c': 0}
    while i <= j < len(st) - 1:
        if st[i] == st[j]:
            if j - i + 1 == k and freq[st[i]] == k:
                count += 1
                j += 1
                freq[s[j]] += 1
            elif j - i + 1 > k:
                freq[s[i]] -= 1
                i += 1
            else:
                j += 1
                freq[s[j]] += 1
        else:
            i = j
            j += 1
            freq[s[j]] += 1

    if st[i] == st[j]:
        count += 1

    return count


if __name__ == '__main__':
    s = "aabbcc"
    k = 2
    print(count_substrings(s, k))
    print(count_substrings_alt(s, k))
    # print(count_substrings(s, k))
