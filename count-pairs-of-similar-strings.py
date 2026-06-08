from typing import List
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        from collections import Counter
        cnt = Counter(frozenset(w) for w in words)
        total = 0
        for v in cnt.values():
            total += v*(v-1)//2
        return total