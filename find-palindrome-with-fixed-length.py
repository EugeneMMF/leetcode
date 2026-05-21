import math
from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength + 1) // 2
        base = 10 ** (half - 1)
        max_count = 9 * (10 ** (half - 1))
        res = []
        for k in queries:
            if k > max_count:
                res.append(-1)
            else:
                first_half = base + (k - 1)
                s = str(first_half)
                if intLength % 2 == 0:
                    pal = s + s[::-1]
                else:
                    pal = s + s[-2::-1]
                res.append(int(pal))
        return res