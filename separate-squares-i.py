class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0.0
        min_y = float('inf')
        max_y = -float('inf')
        for x, y, l in squares:
            area = l * l
            total_area += area
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
        target = total_area / 2.0
        lo, hi = min_y, max_y
        for _ in range(60):
            mid = (lo + hi) / 2
            above = 0.0
            for x, y, l in squares:
                if mid <= y:
                    above += l * l
                elif mid >= y + l:
                    continue
                else:
                    above += (y + l - mid) * l
            if above > target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2.0