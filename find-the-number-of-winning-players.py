from typing import List
from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        counts = [defaultdict(int) for _ in range(n)]
        for x, y in pick:
            counts[x][y] += 1
        res = 0
        for i in range(n):
            for cnt in counts[i].values():
                if cnt > i:
                    res += 1
                    break
        return res
