class Solution:
    def catMouseGame(self, graph):
        from collections import deque
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2
        result = [[[DRAW for _ in range(2)] for _ in range(n)] for _ in range(n)]
        degree = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = sum(1 for nxt in graph[c] if nxt != 0)
        q = deque()
        for i in range(n):
            if i != 0:
                result[0][i][0] = result[0][i][1] = MOUSE
                result[i][i][0] = result[i][i][1] = CAT
                q.append((0, i, 0))
                q.append((0, i, 1))
                q.append((i, i, 0))
                q.append((i, i, 1))
        while q:
            m, c, t = q.popleft()
            cur = result[m][c][t]
            player = t + 1
            prev_t = 1 - t
            if prev_t == 0:
                for pm in graph[m]:
                    if result[pm][c][prev_t] != DRAW:
                        continue
                    if cur == MOUSE:
                        result[pm][c][prev_t] = MOUSE
                        q.append((pm, c, prev_t))
                    else:
                        degree[pm][c][prev_t] -= 1
                        if degree[pm][c][prev_t] == 0:
                            result[pm][c][prev_t] = CAT
                            q.append((pm, c, prev_t))
            else:
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    if result[m][pc][prev_t] != DRAW:
                        continue
                    if cur == CAT:
                        result[m][pc][prev_t] = CAT
                        q.append((m, pc, prev_t))
                    else:
                        degree[m][pc][prev_t] -= 1
                        if degree[m][pc][prev_t] == 0:
                            result[m][pc][prev_t] = MOUSE
                            q.append((m, pc, prev_t))
        return result[1][2][0]
