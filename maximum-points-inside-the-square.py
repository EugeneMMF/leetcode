class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        tag_min = {}
        for (x, y), tag in zip(points, s):
            d = max(abs(x), abs(y))
            if tag not in tag_min:
                tag_min[tag] = [d, float('inf')]
            else:
                if d < tag_min[tag][0]:
                    tag_min[tag][1] = tag_min[tag][0]
                    tag_min[tag][0] = d
                elif d < tag_min[tag][1]:
                    tag_min[tag][1] = d
        min_d2 = float('inf')
        for v in tag_min.values():
            if v[1] != float('inf'):
                if v[1] < min_d2:
                    min_d2 = v[1]
        if min_d2 == float('inf'):
            return len(points)
        cnt = 0
        for x, y in points:
            d = max(abs(x), abs(y))
            if d < min_d2:
                cnt += 1
        return cnt