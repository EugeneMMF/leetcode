from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                neg += 1
        return -1 if neg % 2 else 1
