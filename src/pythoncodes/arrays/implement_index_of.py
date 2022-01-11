def implement_index_of(haystack, needle):
    if needle == '':
        return 0

    n1, n2 = len(haystack), len(needle)
    i = 0
    idx = -1
    while i < n1:
        if haystack[i] == needle[0]:
            idx = i
            j = 0
            while j < n2 and i < n1 and haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == n2:
                break
            else:
                i = idx + 1
                idx = -1
        else:
            i += 1

    return idx


if __name__ == '__main__':
    h = "mississippi"
    n = "issip"

    h1 = "aaabbqbba"
    n1 = "bba"

    h2 = "l"
    n2 = "ll"

    print(implement_index_of(h2, n2))
