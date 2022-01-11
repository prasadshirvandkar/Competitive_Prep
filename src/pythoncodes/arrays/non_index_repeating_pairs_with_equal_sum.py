if __name__ == "__main__":
    nums = [2, 2, 2, 3]
    pairs = {}
    pairs_l = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            pair_sum = nums[i] + nums[j]
            if pair_sum in pairs:
                for v in pairs[pair_sum]:
                    if (v[0] != i and v[0] != j) and (v[1] != i and v[1] != j):
                        pairs[pair_sum].append((i, j))
            else:
                pairs[pair_sum] = [(i, j)]

    count = 0
    for k, v in pairs.items():
        if len(v) >= 2:
            items = set()
            for l in v:
                items.add(l[0])
                items.add(l[1])
                count += 1 if len(items) & 1 == 1 else 2

    print(count)
