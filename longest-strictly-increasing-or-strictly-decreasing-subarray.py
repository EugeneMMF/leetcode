from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        inc = dec = 1
        best = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                inc = 1
            if nums[i] < nums[i-1]:
                dec += 1
            else:
                dec = 1
            best = max(best, inc, dec)
        return best
