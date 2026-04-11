from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0.0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i
        for groups in range(2, k + 1):
            for i in range(groups, n + 1):
                best = 0.0
                for t in range(groups - 1, i):
                    cur = dp[t][groups - 1] + (prefix[i] - prefix[t]) / (i - t)
                    if cur > best:
                        best = cur
                dp[i][groups] = best
        return max(dp[n][j] for j in range(1, k + 1))
