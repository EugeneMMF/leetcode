class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [0, -10**18, -10**18, -10**18, -10**18]
        for val in b:
            for j in range(4, 0, -1):
                dp[j] = max(dp[j], dp[j-1] + a[j-1] * val)
        return dp[4]