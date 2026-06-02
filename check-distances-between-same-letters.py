from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = {}
        for i, ch in enumerate(s):
            if ch in first:
                if i - first[ch] - 1 != distance[ord(ch) - 97]:
                    return False
            else:
                first[ch] = i
        return True
