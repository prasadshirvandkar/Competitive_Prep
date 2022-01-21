def gas_station(gas, cost):
    start_index = 0
    n = len(gas)

    for i in range(len(gas)):
        if (gas[i] - cost[i]) > 0:
            start_index = i
            break

    gas_sum = gas[start_index]
    prev = start_index
    curr_index = start_index + 1
    while True:
        gas_sum = gas_sum - cost[prev % n] + gas[curr_index % n]
        prev = curr_index
        curr_index += 1

        if gas_sum < 0 or gas_sum < cost[prev % n]:
            return -1

        if curr_index % n == start_index:
            break

    return start_index


if __name__ == '__main__':
    g = [1, 2, 3, 4, 5]
    c = [3, 4, 5, 1, 2]

    print(gas_station(g, c))

    g1 = [2, 3, 4]
    c1 = [3, 4, 3]
    print(gas_station(g1, c1))

    g2 = [5, 1, 2, 3, 4]
    c2 = [4, 4, 1, 5, 1]
    print(gas_station(g2, c2))
