
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        
        current_arrow_limit = points[0][1]

        for i in range(1, len(points)):
            xstart, xend = points[i]

            if xstart > current_arrow_limit:
                arrows += 1
                current_arrow_limit = xend
        
        return arrows
