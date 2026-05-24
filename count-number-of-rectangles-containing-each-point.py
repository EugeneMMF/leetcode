class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key=lambda x: x[0], reverse=True)
        points_sorted = sorted([(x, y, idx) for idx, (x, y) in enumerate(points)], key=lambda p: p[0], reverse=True)
        freq = [0] * 101
        res = [0] * len(points)
        r_idx = 0
        for x, y, idx in points_sorted:
            while r_idx < len(rectangles) and rectangles[r_idx][0] >= x:
                hi = rectangles[r_idx][1]
                freq[hi] += 1
                r_idx += 1
            cnt = 0
            for h in range(y, 101):
                cnt += freq[h]
            res[idx] = cnt
        return res