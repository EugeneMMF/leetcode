from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        return [i for i, v in enumerate(sorted_nums) if v == target]
