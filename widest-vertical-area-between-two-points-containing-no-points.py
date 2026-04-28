from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = [p[0] for p in points]
        xs.sort()
        max_gap = 0
        for i in range(1, len(xs)):
            gap = xs[i] - xs[i-1]
            if gap > max_gap:
                max_gap = gap
        return max_gap
