class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x, y, r in queries:
            rr = r * r
            cnt = 0
            for px, py in points:
                dx = px - x
                dy = py - y
                if dx * dx + dy * dy <= rr:
                    cnt += 1
            res.append(cnt)
        return res
