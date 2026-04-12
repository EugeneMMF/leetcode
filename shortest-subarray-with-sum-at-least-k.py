from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pref = [0]
        for v in nums:
            pref.append(pref[-1] + v)
        dq = deque()
        ans = len(nums) + 1
        for i, cur in enumerate(pref):
            while dq and cur - pref[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())
            while dq and cur <= pref[dq[-1]]:
                dq.pop()
            dq.append(i)
        return ans if ans <= len(nums) else -1
