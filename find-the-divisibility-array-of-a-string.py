from typing import List

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        cur = 0
        for ch in word:
            cur = (cur * 10 + (ord(ch) - 48)) % m
            res.append(1 if cur == 0 else 0)
        return res
