from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for w in stones:
            for s in range(target, w - 1, -1):
                dp[s] = dp[s] or dp[s - w]
        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s
        return 0
