from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = neg = 0
        ans = 0
        for x in nums:
            if x == 0:
                pos = neg = 0
            elif x > 0:
                pos += 1
                neg = neg + 1 if neg else 0
            else:
                new_pos = neg + 1 if neg else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            if pos > ans:
                ans = pos
        return ans
