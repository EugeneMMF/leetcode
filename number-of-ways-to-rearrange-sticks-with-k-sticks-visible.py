class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 1000000007
        if k > n or k < 1:
            return 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 0
            maxj = min(i, k)
            for j in range(1, maxj + 1):
                dp[i][j] = (dp[i-1][j-1] + (i-1) * dp[i-1][j]) % MOD
        return dp[n][k]