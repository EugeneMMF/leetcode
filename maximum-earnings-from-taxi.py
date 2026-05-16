class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides_by_start = [[] for _ in range(n + 1)]
        for start, end, tip in rides:
            rides_by_start[start].append((end, tip))
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if dp[i] < dp[i - 1]:
                dp[i] = dp[i - 1]
            for end, tip in rides_by_start[i]:
                profit = end - i + tip
                if dp[end] < dp[i] + profit:
                    dp[end] = dp[i] + profit
        return dp[n]