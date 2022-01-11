# Special Palindrome Substring
import time


def special_palindrome_substring(s):
    specialPalCount = 0
    slen = len(s)
    i = 0
    inc = 1
    start_time = time.time()
    while i < slen:
        if inc > slen:
            i += 1
            inc = i + 1
            continue

        start = i
        end = inc
        inc += 1

        substr = s[start:end]
        isPalin = True

        if s[start] != s[end - 1]:
            continue
        else:
            substrlen = len(substr)
            if substrlen >= 2:
                substrfchar = substr[0]
                for k in range(int(substrlen / 2)):
                    if substr[substrlen - k - 1] != substrfchar or substr[k] != substrfchar:
                        isPalin = False
                        break

            if isPalin:
                # print(substr)
                specialPalCount += 1

    print("--- %s seconds ---" % (time.time() - start_time))
    print(specialPalCount)


if __name__ == '__main__':
    st = "aasasd"
    special_palindrome_substring(st)