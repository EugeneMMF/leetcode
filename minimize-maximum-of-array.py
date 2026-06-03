from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_val = 0
        prefix = 0
        for i, v in enumerate(nums):
            prefix += v
            k = i + 1
            val = (prefix + k - 1) // k
            if val > max_val:
                max_val = val
        return max_val
