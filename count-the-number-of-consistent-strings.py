from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        for w in words:
            if set(w).issubset(allowed_set):
                count += 1
        return count
