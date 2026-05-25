import bisect
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []
        for s in spells:
            idx = bisect.bisect_left(potions, (success + s - 1) // s)
            res.append(m - idx)
        return res
