from heapq import heappush, heappop
from typing import List

weights = [3, 6, 1, 3, 4]
values = [2, 1, 3, 4, 5]
max_weight = 25


def knapsack():
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(len(weights))]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])

    return dp


def maximumTotalWeight(tasks, weights, runtime):
    items = [[tasks[i] * 2, weights[i]] for i in range(len(tasks))]
    knapsackValues = [[0 for _ in range(runtime + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        duration, value = items[i - 1]
        for d in range(1, runtime + 1):
            if duration > d:
                knapsackValues[i][d] = knapsackValues[i - 1][d]
            else:
                knapsackValues[i][d] = max(knapsackValues[i - 1][d], knapsackValues[i - 1][d - duration] + value)
    return knapsackValues[-1][-1]


def maxPerformance(n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    l = list(zip(efficiency, speed))
    l.sort(reverse=True)
    h = []
    res = 0
    mod = 1000000007
    mx_sum = 0
    print(l)
    for i in range(n):
        res = max(res, (mx_sum + l[i][1]) * l[i][0])
        if len(h) < k - 1:
            heappush(h, l[i][1])
            mx_sum += l[i][1]
        elif k != 1:
            x = 0
            if h:
                x = heappop(h)
            heappush(h, max(x, l[i][1]))
            mx_sum = mx_sum - x + max(x, l[i][1])
    return res % mod


if __name__ == "__main__":
    print(maximumTotalWeight(values, weights, 25))
    print(maxPerformance(5, weights, values, 2))
