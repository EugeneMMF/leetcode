import math

class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        if not rectangles:
            return False

        min_x = math.inf
        min_y = math.inf
        max_x = -math.inf
        max_y = -math.inf
        total_area = 0
        
        points = set()

        for rect in rectangles:
            x1, y1, x2, y2 = rect

            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            total_area += (x2 - x1) * (y2 - y1)

            for p_x, p_y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                point = (p_x, p_y)
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)
        
        if len(points) != 4 or \
           (min_x, min_y) not in points or \
           (min_x, max_y) not in points or \
           (max_x, min_y) not in points or \
           (max_x, max_y) not in points:
            return False
        
        if total_area != (max_x - min_x) * (max_y - min_y):
            return False
            
        return True
