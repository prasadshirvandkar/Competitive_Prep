import time


def group_anagrams(strs):
    groups = {}

    for s in strs:
        hashcode = [0 for _ in range(26)]
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            hashcode[c] += 1
        print(hashcode)
        hc = ''.join(str(h) if h < 10 else str(h + 1) for h in hashcode)
        print(hc)
        if hc in groups:
            groups[hc].append(s)
        else:
            groups[hc] = [s]

    return list(groups.values())


if __name__ == '__main__':
    start = time.time()
    strings = ["bdddddddddd", "bbbbbbbbbbc"]
    print(group_anagrams(strings))
    print(str(time.time() - start))

    asd = [["max"], ["buy"], ["doc"], ["may"], ["ill"], ["duh"], ["tin"], ["bar"], ["pew"], ["cab"]]
    op = [["cab"], ["tin"], ["pew"], ["duh", "ill"], ["may"], ["buy"], ["bar"], ["max"], ["doc"]]
