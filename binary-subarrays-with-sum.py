from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        res = 0
        for x in nums:
            prefix += x
            res += count[prefix - goal]
            count[prefix] += 1
        return res
