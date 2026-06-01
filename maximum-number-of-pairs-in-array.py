from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        pairs = sum(v // 2 for v in freq.values())
        leftover = len(nums) - pairs * 2
        return [pairs, leftover]
