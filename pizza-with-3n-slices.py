from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3
        def compute(arr):
            m = len(arr)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                limit = min((i + 1) // 2, n)
                for j in range(1, limit + 1):
                    if i >= 2:
                        take = dp[i - 2][j - 1] + arr[i - 1]
                    else:
                        take = arr[i - 1]
                    dp[i][j] = dp[i - 1][j] if dp[i - 1][j] > take else take
            return dp[m][n]
        return max(compute(slices[:-1]), compute(slices[1:])) 
