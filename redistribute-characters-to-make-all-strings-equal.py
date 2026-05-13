from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        freq = [0] * 26
        for w in words:
            for ch in w:
                freq[ord(ch) - 97] += 1
        for f in freq:
            if f % n != 0:
                return False
        return True
