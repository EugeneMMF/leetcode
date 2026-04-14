class Solution:
    def minAreaFreeRect(self, points):
        n = len(points)
        pts = [tuple(p) for p in points]
        groups = {}
        for i in range(n):
            x1, y1 = pts[i]
            for j in range(i + 1, n):
                x2, y2 = pts[j]
                mx = x1 + x2
                my = y1 + y2
                dx = x1 - x2
                dy = y1 - y2
                d2 = dx * dx + dy * dy
                key = (mx, my, d2)
                groups.setdefault(key, []).append((i, j))
        min_area = float('inf')
        for pair_list in groups.values():
            m = len(pair_list)
            if m < 2:
                continue
            for a in range(m):
                i1, j1 = pair_list[a]
                p1 = pts[i1]
                for b in range(a + 1, m):
                    i2, j2 = pair_list[b]
                    p2 = pts[i2]
                    p3 = pts[j2]
                    # area using p1, p2, p3
                    v1x = p2[0] - p1[0]
                    v1y = p2[1] - p1[1]
                    v2x = p3[0] - p1[0]
                    v2y = p3[1] - p1[1]
                    area = abs(v1x * v2y - v1y * v2x)
                    if area:
                        min_area = min(min_area, area)
        return 0.0 if min_area == float('inf') else float(min_area)
