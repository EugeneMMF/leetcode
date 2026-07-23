from typing import List
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        M = max(nums)
        dp = [0] * (M + 1)
        for v in range(nums[0] + 1):
            dp[v] = 1
        for i in range(1, n):
            prev_max = nums[i - 1]
            cur_max = nums[i]
            delta = cur_max - prev_max
            if delta < 0:
                delta = 0
            pref = [0] * (M + 1)
            s = 0
            for j in range(prev_max + 1):
                s = (s + dp[j]) % mod
                pref[j] = s
            next_dp = [0] * (M + 1)
            for w in range(cur_max + 1):
                idx = w - delta
                if idx >= 0:
                    if idx > prev_max:
                        idx = prev_max
                    next_dp[w] = pref[idx]
            dp = next_dp
        return sum(dp[:nums[-1] + 1]) % mod