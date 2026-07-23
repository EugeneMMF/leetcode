from typing import List

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        current = []
        for ch in target:
            current.append('a')
            res.append(''.join(current))
            inc = ord(ch) - 97
            for _ in range(inc):
                last = current[-1]
                if last == 'z':
                    current[-1] = 'a'
                else:
                    current[-1] = chr(ord(last)+1)
                res.append(''.join(current))
        return res
