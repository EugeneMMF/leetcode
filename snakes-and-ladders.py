class Solution:
    def snakesAndLadders(self, board):
        from collections import deque
        n = len(board)
        target = n * n
        def label_to_pos(label):
            r = n - 1 - (label - 1) // n
            offset = (label - 1) % n
            if ((n - 1 - r) % 2) == 0:
                c = offset
            else:
                c = n - 1 - offset
            return r, c
        visited = [False] * (target + 1)
        q = deque()
        q.append((1, 0))
        visited[1] = True
        while q:
            cur, steps = q.popleft()
            if cur == target:
                return steps
            for d in range(1, 7):
                nxt = cur + d
                if nxt > target:
                    continue
                r, c = label_to_pos(nxt)
                dest = board[r][c] if board[r][c] != -1 else nxt
                if not visited[dest]:
                    visited[dest] = True
                    q.append((dest, steps + 1))
        return -1
