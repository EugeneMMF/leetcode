import typing

class Solution:
    def minRectanglesToCoverPoints(self, points: typing.List[typing.List[int]], w: int) -> int:
        points.sort(key=lambda p: p[0])
        count = 0
        i = 0
        n = len(points)
        while i < n:
            start = points[i][0]
            end = start + w
            count += 1
            i += 1
            while i < n and points[i][0] <= end:
                i += 1
        return count