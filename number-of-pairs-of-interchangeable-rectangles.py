class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        from math import gcd
        counts = {}
        for w, h in rectangles:
            g = gcd(w, h)
            key = (w // g, h // g)
            counts[key] = counts.get(key, 0) + 1
        res = 0
        for c in counts.values():
            res += c * (c - 1) // 2
        return res
