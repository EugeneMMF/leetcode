from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for w in words:
            if s.startswith(w):
                count += 1
        return count
