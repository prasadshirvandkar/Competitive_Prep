from typing import List


def backtrack(nums, curr, res):
    if len(curr) == len(nums):
        res.append(list(curr))
        return

    for i in range(len(nums)):
        if nums[i] in curr:
            continue

        curr.append(nums[i])
        if len(curr) == len(nums):
            res.append(list(curr))
        else:
            backtrack(nums, curr, res)
        curr.pop(-1)

    return res


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return []
    return backtrack(nums, [], [])


if __name__ == '__main__':
    arr = [1, 2, 3]
    print(permute(arr))
