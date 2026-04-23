import math
from typing import List

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        if n == 0:
            return 0
        best = 1
        rr = r * r
        for i in range(n):
            xi, yi = darts[i]
            cnt = 0
            for xj, yj in darts:
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= rr + 1e-7:
                    cnt += 1
            if cnt > best:
                best = cnt
        for i in range(n):
            x1, y1 = darts[i]
            for j in range(i + 1, n):
                x2, y2 = darts[j]
                dx = x2 - x1
                dy = y2 - y1
                d2 = dx * dx + dy * dy
                d = math.hypot(dx, dy)
                if d > 2 * r + 1e-7:
                    continue
                mx = (x1 + x2) / 2.0
                my = (y1 + y2) / 2.0
                h = math.sqrt(max(r * r - (d / 2) ** 2, 0.0))
                ox = -dy / d
                oy = dx / d
                for sign in (1, -1):
                    cx = mx + sign * h * ox
                    cy = my + sign * h * oy
                    cnt = 0
                    for xk, yk in darts:
                        if (cx - xk) ** 2 + (cy - yk) ** 2 <= rr + 1e-7:
                            cnt += 1
                    if cnt > best:
                        best = cnt
        return best
