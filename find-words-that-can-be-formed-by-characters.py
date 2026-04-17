from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0
        for w in words:
            wc = Counter(w)
            for c, cnt in wc.items():
                if char_count.get(c, 0) < cnt:
                    break
            else:
                total += len(w)
        return total
