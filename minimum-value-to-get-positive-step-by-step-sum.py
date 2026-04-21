from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = 0
        cur = 0
        for x in nums:
            cur += x
            if cur < min_prefix:
                min_prefix = cur
        return 1 - min_prefix if min_prefix < 0 else 1
