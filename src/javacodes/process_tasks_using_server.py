import heapq


def process_tasks_using_server(weights, tasks):
    res = []

    heapq.heapify([(weights[i], i) for i in range(len(weights))])
    unavailable_servers = []

    for i in range(len(tasks)):
        if len(unavailable_servers) > 0:
            for server in unavailable_servers:
                if server[0] == i:
                    unavailable_servers.pop(0)
                    break

        poped = heapq.heappop()
        unavailable_servers.append(tuple(i + tasks[i], poped[0], poped[1]))


    return res


if __name__ == '__main__':
    w = [3, 3, 2]
    t = [1, 2, 3, 2, 1, 2]
    print(process_tasks_using_server(w, t))
