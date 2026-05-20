class Solution:
    def highestRankedKItems(self, grid, pricing, start, k):
        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start
        from collections import deque
        q = deque()
        q.append((sr, sc, 0))
        visited = [[False]*n for _ in range(m)]
        visited[sr][sc] = True
        items = []
        while q:
            r, c, d = q.popleft()
            val = grid[r][c]
            if val != 0 and low <= val <= high:
                items.append((d, val, r, c))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, d+1))
        items.sort()
        res = [[r, c] for _, _, r, c in items[:k]]
        return res
