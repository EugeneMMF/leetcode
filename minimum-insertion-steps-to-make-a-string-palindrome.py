class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        rev = s[::-1]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if s[i - 1] == rev[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = dp[j] if dp[j] > dp[j - 1] else dp[j - 1]
                prev = temp
        return n - dp[n]
