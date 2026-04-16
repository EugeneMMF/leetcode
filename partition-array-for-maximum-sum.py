from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_val = 0
            for j in range(1, min(k, i) + 1):
                if arr[i - j] > max_val:
                    max_val = arr[i - j]
                cur = dp[i - j] + max_val * j
                if cur > dp[i]:
                    dp[i] = cur
        return dp[n]
