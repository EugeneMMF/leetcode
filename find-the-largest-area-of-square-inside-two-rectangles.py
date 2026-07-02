class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        for i in range(n):
            ax, ay = bottomLeft[i]
            cx, cy = topRight[i]
            for j in range(i + 1, n):
                bx, by = bottomLeft[j]
                dx, dy = topRight[j]
                ix1 = ax if ax > bx else bx
                iy1 = ay if ay > by else by
                ix2 = cx if cx < dx else dx
                iy2 = cy if cy < dy else dy
                if ix1 < ix2 and iy1 < iy2:
                    side = ix2 - ix1 if ix2 - ix1 < iy2 - iy1 else iy2 - iy1
                    if side > max_side:
                        max_side = side
        return max_side * max_side
