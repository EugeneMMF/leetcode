from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1
        for x in nums[1:]:
            if x > min_val:
                diff = x - min_val
                if diff > max_diff:
                    max_diff = diff
            if x < min_val:
                min_val = x
        return max_diff
