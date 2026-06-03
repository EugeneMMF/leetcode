class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            best = 1
            max_len = (n - i) // 2
            for l in range(1, max_len + 1):
                if s[i:i + l] == s[i + l:i + 2 * l]:
                    best = max(best, 1 + dp[i + l])
            dp[i] = best
        return dp[0]