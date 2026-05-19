from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        j = 0
        m = len(spaces)
        for i, ch in enumerate(s):
            if j < m and i == spaces[j]:
                res.append(' ')
                j += 1
            res.append(ch)
        return ''.join(res)
