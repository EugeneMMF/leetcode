class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [grid[0][j] for j in range(n)]
        for i in range(1, m):
            new = [0] * n
            for j in range(n):
                best = 10**12
                for k in range(n):
                    cost = dp[k] + moveCost[grid[i - 1][k]][j] + grid[i][j]
                    if cost < best:
                        best = cost
                new[j] = best
            dp = new
        return min(dp)