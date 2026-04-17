from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        if not q or len(q) == n * n:
            return -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_dist = -1
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = grid[x][y] + 1
                    max_dist = max(max_dist, grid[nx][ny] - 1)
                    q.append((nx, ny))
        return max_dist
