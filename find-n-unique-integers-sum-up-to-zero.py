from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        half = n // 2
        for i in range(1, half + 1):
            res.append(i)
            res.append(-i)
        if n % 2:
            res.append(0)
        return res[:n]
