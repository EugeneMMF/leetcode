from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        for pile in piles:
            prefix = [0]
            for v in pile:
                prefix.append(prefix[-1] + v)
            m = min(k, len(pile))
            new_dp = dp[:]
            for j in range(1, m + 1):
                val = prefix[j]
                for t in range(k, j - 1, -1):
                    if dp[t - j] + val > new_dp[t]:
                        new_dp[t] = dp[t - j] + val
            dp = new_dp
        return dp[k]
