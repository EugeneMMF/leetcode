from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_left = nums[0]
        overall_max = nums[0]
        partition = 0
        for i in range(1, len(nums)):
            overall_max = max(overall_max, nums[i])
            if nums[i] < max_left:
                partition = i
                max_left = overall_max
        return partition + 1
