import typing

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: typing.List[typing.List[int]]) -> int:
        bestDist = float('inf')
        bestIndex = -1
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                dist = abs(a - x) + abs(b - y)
                if dist < bestDist:
                    bestDist = dist
                    bestIndex = i
        return bestIndex
