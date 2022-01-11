graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()


def detect_cycle(v):
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            detect_cycle(i)
        else:
            print(f'Cycle Detected at: {i}')


if __name__ == '__main__':
    detect_cycle('A')
