from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = set(days)
        last = days[-1]
        dp = [0] * (last + 1)
        for d in range(1, last + 1):
            if d not in travel:
                dp[d] = dp[d - 1]
            else:
                cost1 = dp[d - 1] + costs[0]
                cost7 = dp[max(0, d - 7)] + costs[1]
                cost30 = dp[max(0, d - 30)] + costs[2]
                dp[d] = min(cost1, cost7, cost30)
        return dp[last]
