class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for ch in s:
            idx = ord(ch) - 97
            l = max(0, idx - k)
            r = min(25, idx + k)
            best = 0
            for j in range(l, r + 1):
                if dp[j] > best:
                    best = dp[j]
            dp[idx] = best + 1
        return max(dp)