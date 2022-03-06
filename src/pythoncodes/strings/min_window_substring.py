import sys
from collections import defaultdict


def min_window_substring(s, pat):
    pat_map, s_map = defaultdict(), defaultdict()

    for pt in pat:
        pat_map[pt] = pat_map.get(pt, 0) + 1

    count, idx, start_index, end_index = 0, 0, 0, 0
    min_window = sys.maxsize

    for i in range(len(s)):
        s_map[s[i]] = s_map.get(s[i], 0) + 1

        if s[i] in pat_map and s_map[s[i]] <= pat_map[s[i]]:
            count += 1

        if count == len(pat):
            while s[idx] not in pat_map or s_map[s[idx]] > pat_map[s[idx]]:
                st_at_idx = s[idx]
                if st_at_idx not in pat_map or s_map[st_at_idx] > pat_map[st_at_idx]:
                    s_map[st_at_idx] -= 1
                    if s_map[st_at_idx] == 0:
                        s_map.pop(st_at_idx)
                idx += 1

            curr_window = i - idx + 1
            if curr_window < min_window:
                min_window = curr_window
                start_index = idx
                end_index = i

    return min_window, start_index, end_index


if __name__ == '__main__':
    st = 'codebanced'
    p = 'abc'
    window_size, start, end = min_window_substring(st, p)
    print(window_size)
    print(st[start:end + 1])
