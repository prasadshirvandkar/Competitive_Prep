def paint_house(cost):
    min_cost = 0
    curr = -1

    curr_cost = 123123123
    for i in range(0, len(cost)):
        for j in range(0, 3):
            if cost[i][j] < curr_cost and j != curr:
                curr = j
                curr_cost = cost[i][j]
        min_cost += curr_cost
        curr_cost = 123123123

    return min_cost


if __name__ == '__main__':
    colors = [
        [14, 2, 11],
        [11, 14, 5],
        [14, 3, 10]
    ]

    colors1 = [
        [1, 2, 3],
        [1, 4, 6]
    ]

    print(paint_house(colors1))
