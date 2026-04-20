from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        counts = sorted(freq.values(), reverse=True)
        target = len(arr) // 2
        removed = 0
        ans = 0
        for c in counts:
            removed += c
            ans += 1
            if removed >= target:
                return ans
