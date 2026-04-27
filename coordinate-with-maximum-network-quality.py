class Solution:
    def bestCoordinate(self, towers, radius):
        import math
        max_x = max(t[0] for t in towers) + radius
        max_y = max(t[1] for t in towers) + radius
        best = [0, 0]
        best_val = -1
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                total = 0
                for tx, ty, q in towers:
                    dx = tx - x
                    dy = ty - y
                    d = math.hypot(dx, dy)
                    if d <= radius:
                        total += int(q // (1 + d))
                if total > best_val or (total == best_val and (x < best[0] or (x == best[0] and y < best[1]))):
                    best_val = total
                    best = [x, y]
        return best
