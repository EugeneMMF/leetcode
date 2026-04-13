class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(goal):
            for j in range(n + 1):
                val = dp[i][j]
                if not val:
                    continue
                if j < n:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + val * (n - j)) % MOD
                if j > k:
                    dp[i + 1][j] = (dp[i + 1][j] + val * (j - k)) % MOD
        return dp[goal][n]
