class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        point_set = {tuple(p) for p in points}
        xs = sorted({p[0] for p in points})
        ys = sorted({p[1] for p in points})
        max_area = -1
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                x1, x2 = xs[i], xs[j]
                for k in range(len(ys)):
                    for l in range(k + 1, len(ys)):
                        y1, y2 = ys[k], ys[l]
                        corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
                        if not corners.issubset(point_set):
                            continue
                        valid = True
                        for p in point_set:
                            if p in corners:
                                continue
                            px, py = p
                            if x1 <= px <= x2 and y1 <= py <= y2:
                                valid = False
                                break
                        if valid:
                            area = (x2 - x1) * (y2 - y1)
                            if area > max_area:
                                max_area = area
        return max_area