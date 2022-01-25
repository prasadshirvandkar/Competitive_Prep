board = [
    ['C', 'A', 'T'],
    ['I', 'D', 'O'],
    ['M', 'O', 'M']
]


def dfs(count, r, c, word, visited):
    if count == len(word):
        return True

    if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
        return False

    if str(r) + str(c) in visited or word[count] != board[r][c]:
        return False

    visited.add(str(r) + str(c))

    if dfs(count + 1, r, c - 1, word, visited):
        return True

    if dfs(count + 1, r, c + 1, word, visited):
        return True

    if dfs(count + 1, r - 1, c, word, visited):
        return True

    if dfs(count + 1, r + 1, c, word, visited):
        return True


def word_search(words):
    res = []
    for word in words:
        print(word)
        visited = set()
        temp = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp = True if dfs(0, i, j, word, visited) else False
        res.append(temp)
    return res


def findWords(letters, words):
    trie,  ans, m, n = {}, set(), len(letters), len(letters) and len(letters[0])
    for word in words:
        node = trie
        for w in word:
            node = node.setdefault(w, {})
        node['$'] = None

    def dfs(i, j, node, word):
        if letters[i][j] in node:
            letters[i][j], c = '', letters[i][j]
            node, word = node[c], word + c
            if '$' in node:
                ans.add(word)
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n:
                    dfs(x, y, node, word)
            letters[i][j] = c

    for i in range(m):
        for j in range(n):
            dfs(i, j, trie, '')

    return ['Yes' if word in ans else 'No' for word in words]


if __name__ == '__main__':
    w = ['CAT', 'TOM', 'ADO', 'MOM', 'CDM']
    letters = [
        ['C', 'A', 'T'],
        ['I', 'D', 'O'],
        ['M', 'O', 'M']
    ]

    print(findWords(letters, w))
