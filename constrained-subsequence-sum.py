from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dq = deque()
        ans = -10**9
        for i in range(n):
            if dq and dq[0][0] < i - k:
                dq.popleft()
            best = dq[0][1] if dq else 0
            dp[i] = nums[i] + (best if best > 0 else 0)
            if dp[i] > ans:
                ans = dp[i]
            while dq and dq[-1][1] <= dp[i]:
                dq.pop()
            dq.append((i, dp[i]))
        return ans
