from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        cur = 0
        for g in gain:
            cur += g
            if cur > max_alt:
                max_alt = cur
        return max_alt
