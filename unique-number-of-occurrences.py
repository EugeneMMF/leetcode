from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        seen = set()
        for v in freq.values():
            if v in seen:
                return False
            seen.add(v)
        return True
