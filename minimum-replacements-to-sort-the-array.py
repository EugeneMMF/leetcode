from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        cur_max = 10**18
        for x in reversed(nums):
            if x <= cur_max:
                cur_max = x
            else:
                parts = (x + cur_max - 1) // cur_max
                ops += parts - 1
                cur_max = x // parts
        return ops
