class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            best = 1 + dp[i + 1]
            for w in dictionary:
                l = len(w)
                if i + l <= n and s[i:i + l] == w:
                    best = min(best, dp[i + l])
            dp[i] = best
        return dp[0]
