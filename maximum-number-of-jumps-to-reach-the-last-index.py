from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-10**9] * n
        dp[0] = 0
        for i in range(1, n):
            best = -10**9
            for j in range(i):
                if abs(nums[i] - nums[j]) <= target:
                    if dp[j] + 1 > best:
                        best = dp[j] + 1
            dp[i] = best
        return dp[-1] if dp[-1] > 0 else -1
