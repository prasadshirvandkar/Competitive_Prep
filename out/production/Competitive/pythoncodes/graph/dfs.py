graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph1_h5 = {
    'A': ['B', 'G', 'H', 'I'],
    'B': ['A', 'C', 'D', 'E', 'F', 'I'],
    'C': ['B', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['B', 'C'],
    'G': ['A', 'H'],
    'H': ['A', 'G'],
    'I': ['A', 'B']
}

graph1_sm = {
    'A': ['B', 'I'],
    'B': ['A', 'C', 'D', 'E', 'F', 'I'],
    'C': ['B', 'D'],
    'D': ['B', 'C'],
    'E': ['B', 'F'],
    'F': ['B', 'E'],
    'G': ['H', 'I'],
    'H': ['G', 'I'],
    'I': ['A', 'B', 'G', 'H']
}

r_visited = set()


def perform_dfs():
    visited = set()
    stack = ['A']
    while len(stack) > 0:
        s = stack.pop()

        if s not in visited:
            print(s)
            visited.add(s)

        for item in graph[s]:
            if item not in visited:
                stack.append(item)


def dfs_rec(v):
    r_visited.add(v)
    print(v)
    for i in graph1_h5[v]:
        if i not in r_visited:
            dfs_rec(i)


if __name__ == '__main__':
    perform_dfs()
    print('DFS Recursion: \n')
    dfs_rec('A')
