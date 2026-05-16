class Solution:
    def placeWordInCrossword(self, board, word):
        m, n = len(board), len(board[0])
        wlen = len(word)
        rev = word[::-1]
        for i in range(m):
            j = 0
            while j < n:
                if board[i][j] == '#':
                    j += 1
                    continue
                start = j
                while j < n and board[i][j] != '#':
                    j += 1
                end = j - 1
                length = end - start + 1
                if length == wlen:
                    ok = True
                    for k in range(wlen):
                        if board[i][start + k] != ' ' and board[i][start + k] != word[k]:
                            ok = False
                            break
                    if ok:
                        left = board[i][start - 1] if start - 1 >= 0 else '#'
                        right = board[i][end + 1] if end + 1 < n else '#'
                        if left == '#' and right == '#':
                            return True
                    ok = True
                    for k in range(wlen):
                        if board[i][start + k] != ' ' and board[i][start + k] != rev[k]:
                            ok = False
                            break
                    if ok:
                        left = board[i][start - 1] if start - 1 >= 0 else '#'
                        right = board[i][end + 1] if end + 1 < n else '#'
                        if left == '#' and right == '#':
                            return True
        for j in range(n):
            i = 0
            while i < m:
                if board[i][j] == '#':
                    i += 1
                    continue
                start = i
                while i < m and board[i][j] != '#':
                    i += 1
                end = i - 1
                length = end - start + 1
                if length == wlen:
                    ok = True
                    for k in range(wlen):
                        if board[start + k][j] != ' ' and board[start + k][j] != word[k]:
                            ok = False
                            break
                    if ok:
                        above = board[start - 1][j] if start - 1 >= 0 else '#'
                        below = board[end + 1][j] if end + 1 < m else '#'
                        if above == '#' and below == '#':
                            return True
                    ok = True
                    for k in range(wlen):
                        if board[start + k][j] != ' ' and board[start + k][j] != rev[k]:
                            ok = False
                            break
                    if ok:
                        above = board[start - 1][j] if start - 1 >= 0 else '#'
                        below = board[end + 1][j] if end + 1 < m else '#'
                        if above == '#' and below == '#':
                            return True
        return False