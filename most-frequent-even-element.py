from collections import Counter
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter(x for x in nums if x % 2 == 0)
        if not freq:
            return -1
        max_count = max(freq.values())
        candidates = [x for x, c in freq.items() if c == max_count]
        return min(candidates)
