class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * 16 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if i == 0 and j == 0:
                    dp[i][j][val] = 1
                else:
                    cur = dp[i][j]
                    if i > 0:
                        prev = dp[i - 1][j]
                        for x in range(16):
                            cnt = prev[x]
                            if cnt:
                                cur[x ^ val] = (cur[x ^ val] + cnt) % MOD
                    if j > 0:
                        prev = dp[i][j - 1]
                        for x in range(16):
                            cnt = prev[x]
                            if cnt:
                                cur[x ^ val] = (cur[x ^ val] + cnt) % MOD
        return dp[m - 1][n - 1][k] % MOD