#!/usr/bin/env python3
import re


def sum_odd_even(arr):
    odd, even = 0, 1
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even *= arr[i]
        else:
            odd += arr[i]

    return odd, even


def conv_screaming_snake_case(st):
    new_st = ''
    for s in st:
        new_st += '_' if s == '-' else s.upper()

    return new_st


def parts_of_parts(prod):
    parts = {
        'A': ['B', 'B', 'C'],
        'B': [],
        'C': ['D', 'E', 'F'],
        'D': [],
        'E': ['B', 'D'],
        'F': []
    }
    if prod in parts:
        stack = parts[prod]
        if len(stack) == 0:
            return {prod: 1}

        total_parts = []
        while len(stack) > 0:
            part = stack.pop(0)
            if part in parts:
                p = parts[part]
                if len(p) == 0:
                    total_parts.append(part)
                for i in range(len(p)):
                    stack.append(p[i])

        total_parts_map = dict()
        for tp in total_parts:
            total_parts_map[tp] = total_parts_map.get(tp, 0) + 1

        return total_parts_map

    return {}


def parts_of_parts_recursive(prod, total_parts, parts):
    if prod in parts:
        part = parts[prod]
        if len(part) == 0:
            total_parts.append(prod)
            return

        for i in range(len(part)):
            parts_of_parts_recursive(part[i], total_parts, parts)

    return


def parts_of_parts_rec(prod):
    parts = {
        'A': ['B', 'B', 'C'],
        'B': [],
        'C': ['D', 'E', 'F'],
        'D': [],
        'E': ['B', 'D'],
        'F': []
    }
    total_parts = []
    parts_of_parts_recursive(prod, total_parts, parts)
    total_parts_map = dict()
    for t in total_parts:
        total_parts_map[t] = total_parts_map.get(t, 0) + 1

    return total_parts_map


def search_words(words):
    to_match = ['odoo', 'oxp', 'openerp']
    matches = []
    for word in words:
        for match in to_match:
            if re.match(r'^#' + match + '|' + match, word):
                matches.append(word)
                break

    return matches


def asf(A):
    odd_sum, even_sum, x, y = 0, 0, 0, 0

    for i in range(len(A)):
        if i % 2 == 0:
            if x % 2 == 0:
                even_sum += A[i]
            else:
                even_sum *= A[i]
            x += 1
        else:
            if y % 2 == 0:
                odd_sum += A[i]
            else:
                odd_sum *= A[i]
            y += 1

    x = even_sum % 2
    y = odd_sum % 2

    if x > y:
        print("EVEN")
    elif x < y:
        print("ODD")
    else:
        print("NEUTRAL")

    return 0


def longestCon(n, h):
    count, prev = 0, 0
    for i in range(n + 1):
        if i + 1 not in h:
            count = max(count, (i + 1) - prev)
            prev = i + 1

    return count if count > 0 else n + 1


def prison(n, m, h, v):
    x = [1 for _ in range(n + 1)]
    y = [1 for _ in range(m + 1)]

    for i in range(len(h)):
        x[h[i]] = 0

    for i in range(len(v)):
        y[v[i]] = 0

    cx, cy, ox, oy = 0, 0, -1, -1

    for i in range(1, n + 1):
        if x[i] == 1:
            cx = 0
        else:
            cx += 1
            ox = max(ox, cx)

    for i in range(1, m + 1):
        if y[i] == 1:
            cy = 0
        else:
            cy += 1
            oy = max(oy, cy)

    print((ox + 1) * (oy + 1))


if __name__ == "__main__":
    print(prison(3, 2, [1, 2, 3], [1]))
