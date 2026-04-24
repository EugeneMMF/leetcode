from typing import List
import math

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)
        for _ in range(10000):
            num_x = num_y = den = 0.0
            for px, py in positions:
                dx = x - px
                dy = y - py
                dist = math.hypot(dx, dy)
                if dist < 1e-12:
                    x, y = px, py
                    break
                w = 1.0 / dist
                num_x += px * w
                num_y += py * w
                den += w
            else:
                new_x = num_x / den
                new_y = num_y / den
                if math.hypot(new_x - x, new_y - y) < 1e-7:
                    x, y = new_x, new_y
                    break
                x, y = new_x, new_y
        return sum(math.hypot(x - px, y - py) for px, py in positions)
