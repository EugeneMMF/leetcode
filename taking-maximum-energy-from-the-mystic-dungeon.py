from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        ans = -10**18
        for i in range(n - 1, -1, -1):
            nxt = i + k
            if nxt < n:
                dp[i] = energy[i] + dp[nxt]
            else:
                dp[i] = energy[i]
            if dp[i] > ans:
                ans = dp[i]
        return ans
