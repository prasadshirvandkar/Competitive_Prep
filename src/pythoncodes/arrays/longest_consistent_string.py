# Consistent String - The Longest String with Starting and Ending letter matched
def find_consistent_string(s):
    s_list = []
    for i in range(0, len(s)):
        c = s[i]
        for j in reversed(range(i + 1, len(s))):
            if c == s[j]:
                start = i
                end = j + 1
                s_list.append((start, end))
                break

    consistent_str = s[0:1]
    if len(s_list) > 0:
        s_list.sort(key=lambda x: x[0])
        start, end = s_list[0][0], s_list[0][1]
        consistent_str = s[start:end]
    print(consistent_str)


if __name__ == "__main__":
    st = 'performance'
    find_consistent_string(st)
