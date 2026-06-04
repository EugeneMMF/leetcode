from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for x in nums:
            if x % 2 == 0 and x % 3 == 0:
                total += x
                count += 1
        return total // count if count else 0
