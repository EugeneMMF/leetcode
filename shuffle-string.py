from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for ch, idx in zip(s, indices):
            res[idx] = ch
        return ''.join(res)
