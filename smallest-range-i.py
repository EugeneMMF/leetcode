from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)
        diff = mx - mn - 2 * k
        return diff if diff > 0 else 0
