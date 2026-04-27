class Solution:
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if i == 0 and j == 0:
                    max_dp[i][j] = min_dp[i][j] = val
                else:
                    candidates = []
                    if i > 0:
                        candidates.append(max_dp[i-1][j])
                        candidates.append(min_dp[i-1][j])
                    if j > 0:
                        candidates.append(max_dp[i][j-1])
                        candidates.append(min_dp[i][j-1])
                    max_val = -10**20
                    min_val = 10**20
                    for prev in candidates:
                        prod = prev * val
                        if prod > max_val:
                            max_val = prod
                        if prod < min_val:
                            min_val = prod
                    max_dp[i][j] = max_val
                    min_dp[i][j] = min_val
        res = max_dp[m-1][n-1]
        return -1 if res < 0 else res % MOD
