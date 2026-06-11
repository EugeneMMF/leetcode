from typing import List

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: x[0])
        mod = 10**9 + 7
        comps = 0
        cur_end = -1
        for s, e in ranges:
            if s > cur_end:
                comps += 1
                cur_end = e
            else:
                if e > cur_end:
                    cur_end = e
        return pow(2, comps, mod)
