from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        res = []
        cur = 2
        while finalSum >= cur:
            res.append(cur)
            finalSum -= cur
            cur += 2
        if finalSum > 0:
            res[-1] += finalSum
        return res
