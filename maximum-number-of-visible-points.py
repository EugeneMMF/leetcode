class Solution:
    def visiblePoints(self, points, angle, location):
        import math
        x0, y0 = location
        same = 0
        angles = []
        for x, y in points:
            dx, dy = x - x0, y - y0
            if dx == 0 and dy == 0:
                same += 1
            else:
                a = math.degrees(math.atan2(dy, dx))
                if a < 0:
                    a += 360
                angles.append(a)
        if not angles:
            return same
        if angle >= 360:
            return same + len(angles)
        angles.sort()
        extended = angles + [a + 360 for a in angles]
        max_cnt = 0
        j = 0
        n = len(angles)
        for i in range(n):
            while j < i + n and extended[j] - extended[i] <= angle + 1e-9:
                j += 1
            max_cnt = max(max_cnt, j - i)
        return same + max_cnt
