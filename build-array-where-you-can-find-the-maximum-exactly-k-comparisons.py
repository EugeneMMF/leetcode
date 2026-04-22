class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        if k == 0:
            return 0
        dp = [[[0] * (m + 1) for _ in range(k + 2)] for _ in range(n + 1)]
        for x in range(1, m + 1):
            dp[1][1][x] = 1
        for i in range(1, n):
            for j in range(1, k + 1):
                for x in range(1, m + 1):
                    val = dp[i][j][x]
                    if not val:
                        continue
                    dp[i + 1][j][x] = (dp[i + 1][j][x] + val * x) % MOD
                    if j + 1 <= k:
                        add = val
                        for y in range(x + 1, m + 1):
                            dp[i + 1][j + 1][y] = (dp[i + 1][j + 1][y] + add) % MOD
        ans = sum(dp[n][k][x] for x in range(1, m + 1)) % MOD
        return ans
