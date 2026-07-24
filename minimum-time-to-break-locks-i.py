from typing import List

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        n = len(strength)
        full_mask = (1 << n) - 1
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            cnt = bin(mask).count('1')
            x = 1 + cnt * k
            for i in range(n):
                if not (mask & (1 << i)):
                    need = (strength[i] + x - 1) // x
                    new_mask = mask | (1 << i)
                    if dp[new_mask] > dp[mask] + need:
                        dp[new_mask] = dp[mask] + need
        return dp[full_mask]