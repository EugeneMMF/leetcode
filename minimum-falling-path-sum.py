from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [row[:] for row in matrix]
        for i in range(1, n):
            for j in range(n):
                best = dp[i-1][j]
                if j > 0:
                    best = best if best < dp[i-1][j-1] else dp[i-1][j-1]
                if j < n - 1:
                    best = best if best < dp[i-1][j+1] else dp[i-1][j+1]
                dp[i][j] += best
        return min(dp[-1])
