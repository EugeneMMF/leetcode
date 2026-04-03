import math

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        point_set = set()
        for x, y in points:
            point_set.add((x, y))

        min_area = math.inf

        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                p1_x, p1_y = points[i]
                p2_x, p2_y = points[j]

                if p1_x == p2_x or p1_y == p2_y:
                    continue

                if (p1_x, p2_y) in point_set and (p2_x, p1_y) in point_set:
                    current_area = abs(p2_x - p1_x) * abs(p2_y - p1_y)
                    min_area = min(min_area, current_area)

        if min_area == math.inf:
            return 0
        else:
            return min_area
