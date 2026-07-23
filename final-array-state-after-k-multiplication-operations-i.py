from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_idx = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[min_idx]:
                    min_idx = i
            nums[min_idx] *= multiplier
        return nums
