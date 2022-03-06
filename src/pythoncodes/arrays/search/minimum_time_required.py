#https://www.hackerrank.com/challenges/minimum-time-required/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
import math
import sys


def min_time_required(goal, machines):
    min_time = sys.maxsize
    low, high = 0, math.prod(machines)
    while low < high:
        mid = (low + high) // 2
        time = sum([mid // mc for mc in machines])
        if time == goal:
            min_time = min(mid, min_time)

        if time >= goal:
            high = mid
        else:
            low = mid + 1

    mid = (low + high) // 2
    time = sum([mid // mc for mc in machines])
    if time == goal:
        min_time = min(mid, min_time)

    return min_time


if __name__ == '__main__':
    g1 = 5
    m1 = [2, 3]
    print(min_time_required(g1, m1))

    g2 = 12
    m2 = [4, 5, 6]
    print(min_time_required(g2, m2))

    g3 = 10
    m3 = [1, 3, 4]
    print(min_time_required(g3, m3))
