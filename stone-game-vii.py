class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stones[i]
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                sum_left = pref[j + 1] - pref[i + 1]
                sum_right = pref[j] - pref[i]
                dp[i][j] = max(sum_left - dp[i + 1][j], sum_right - dp[i][j - 1])
        return dp[0][n - 1]


