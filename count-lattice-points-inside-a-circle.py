class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        import math
        min_x = min(cx - r for cx, cy, r in circles)
        max_x = max(cx + r for cx, cy, r in circles)
        min_y = min(cy - r for cx, cy, r in circles)
        max_y = max(cy + r for cx, cy, r in circles)
        min_x = max(min_x, 0)
        max_x = min(max_x, 200)
        min_y = max(min_y, 0)
        max_y = min(max_y, 200)
        points = set()
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for cx, cy, r in circles:
                    dx = x - cx
                    dy = y - cy
                    if dx * dx + dy * dy <= r * r:
                        points.add((x, y))
                        break
        return len(points)
