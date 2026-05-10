from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                needed = prev + 1
                ops += needed - nums[i]
                prev = needed
            else:
                prev = nums[i]
        return ops
