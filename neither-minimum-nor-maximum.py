from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        mn = min(nums)
        mx = max(nums)
        for num in nums:
            if num != mn and num != mx:
                return num
        return -1
