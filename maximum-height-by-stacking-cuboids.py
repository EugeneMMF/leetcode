from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()
        cuboids.sort()
        n = len(cuboids)
        dp = [0] * n
        res = 0
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    if dp[j] + cuboids[i][2] > dp[i]:
                        dp[i] = dp[j] + cuboids[i][2]
            if dp[i] > res:
                res = dp[i]
        return res
