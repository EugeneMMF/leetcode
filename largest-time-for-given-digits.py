class Solution:
    def largestTimeFromDigits(self, arr):
        from itertools import permutations
        best = -1
        for p in permutations(arr):
            h = p[0] * 10 + p[1]
            m = p[2] * 10 + p[3]
            if 0 <= h < 24 and 0 <= m < 60:
                total = h * 60 + m
                if total > best:
                    best = total
        if best == -1:
            return ""
        h, m = divmod(best, 60)
        return f"{h:02d}:{m:02d}"
