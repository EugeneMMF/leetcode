from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        max_k = -1
        for x in nums:
            if x > 0 and -x in s:
                if x > max_k:
                    max_k = x
        return max_k
