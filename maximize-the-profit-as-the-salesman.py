class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[1])
        ends = [e for _, e, _ in offers]
        from bisect import bisect_right
        dp = [0] * (len(offers) + 1)
        for i, (s, e, g) in enumerate(offers, 1):
            p = bisect_right(ends, s - 1)
            dp[i] = max(dp[i - 1], dp[p] + g)
        return dp[-1]