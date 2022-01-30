import sys


def is_valid(mat, r, c, visited):
    return 0 <= r < len(mat) and 0 <= c < len(mat[0]) and str(r) + str(c) not in visited and mat[r][c] == 1


def dfs(mat, r, c, visited, dist, dest, min_dist):
    if (r, c) == dest:
        return min(dist, min_dist)

    visited.add(str(r) + str(c))

    if is_valid(mat, r - 1, c, visited):
        min_dist = dfs(mat, r - 1, c, visited, dist + 1, dest, min_dist)

    if is_valid(mat, r + 1, c, visited):
        min_dist = dfs(mat, r + 1, c, visited, dist + 1, dest, min_dist)

    if is_valid(mat, r, c - 1, visited):
        min_dist = dfs(mat, r, c - 1, visited, dist + 1, dest, min_dist)

    if is_valid(mat, r, c + 1, visited):
        min_dist = dfs(mat, r, c + 1, visited, dist + 1, dest, min_dist)

    visited.remove(str(r) + str(c))

    return min_dist


def shortest_path_in_maze(mat, dest):
    if not mat or len(mat) == 0 or mat[dest[0]][dest[1]] == 0:
        return -1

    return dfs(mat, 0, 0, set(), 0, dest, 123123123)


if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]

    source = (0, 0)
    destination = (7, 5)

    print(shortest_path_in_maze(matrix, destination))