from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for j in range(n - 2, -1, -1):
            for i in range(m):
                best = 0
                val = grid[i][j]
                if i > 0 and grid[i - 1][j + 1] > val:
                    best = max(best, 1 + dp[i - 1][j + 1])
                if grid[i][j + 1] > val:
                    best = max(best, 1 + dp[i][j + 1])
                if i < m - 1 and grid[i + 1][j + 1] > val:
                    best = max(best, 1 + dp[i + 1][j + 1])
                dp[i][j] = best
        ans = 0
        for i in range(m):
            ans = max(ans, dp[i][0])
        return ans
