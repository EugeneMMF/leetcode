from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        for l, w in rectangles:
            side = l if l < w else w
            if side > max_len:
                max_len = side
        cnt = 0
        for l, w in rectangles:
            if (l if l < w else w) == max_len:
                cnt += 1
        return cnt
