import sys
from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9+7
        m, n = len(grid), len(grid[0])
        cells = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort()
        dp = [[0]*n for _ in range(m)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for val, i, j in cells:
            total = 1
            for di,dj in dirs:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] < val:
                    total = (total + dp[ni][nj])%MOD
            dp[i][j] = total
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dp[i][j])%MOD
        return ans
