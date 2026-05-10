from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [0, 1, 0, 1]
        n = len(obstacles) - 1
        for i in range(1, n + 1):
            if obstacles[i] != 0:
                dp[obstacles[i]] = float('inf')
            min_jump = min(dp[l] for l in range(1, 4) if obstacles[i] != l)
            for l in range(1, 4):
                if obstacles[i] != l:
                    dp[l] = min(dp[l], min_jump + 1)
        return min(dp[1], dp[2], dp[3])