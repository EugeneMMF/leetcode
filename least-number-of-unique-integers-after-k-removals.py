from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        counts = sorted(freq.values())
        unique = len(counts)
        i = 0
        while i < len(counts) and k >= counts[i]:
            k -= counts[i]
            unique -= 1
            i += 1
        return unique
