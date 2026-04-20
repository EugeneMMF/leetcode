class Solution:
    def minCost(self, grid):
        from collections import deque
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[10**9] * n for _ in range(m)]
        dq = deque()
        dist[0][0] = 0
        dq.append((0, 0))
        while dq:
            i, j = dq.popleft()
            d = dist[i][j]
            if i == m - 1 and j == n - 1:
                continue
            for idx, (dx, dy) in enumerate(dirs, 1):
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    w = 0 if grid[i][j] == idx else 1
                    nd = d + w
                    if nd < dist[ni][nj]:
                        dist[ni][nj] = nd
                        if w == 0:
                            dq.appendleft((ni, nj))
                        else:
                            dq.append((ni, nj))
        return dist[m - 1][n - 1]
