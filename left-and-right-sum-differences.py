from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        prefix = 0
        res = []
        for num in nums:
            left = prefix
            right = total - prefix - num
            res.append(abs(left - right))
            prefix += num
        return res
