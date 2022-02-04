from typing import List


def backtrack(nums, curr, res, check):
    for i in range(len(nums)):
        if i in check:
            continue

        curr.append(nums[i])
        check.add(i)
        if len(curr) == len(nums) and curr not in res:
            res.append(list(curr))
        else:
            backtrack(nums, curr, res, check)
        curr.pop(-1)
        check.remove(i)

    return res


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return []
    return backtrack(nums, [], [], set())


if __name__ == '__main__':
    arr = [1, 1, 2]
    print(permute(arr))
    arr1 = [1, 2, 3]
    print(permute(arr1))
