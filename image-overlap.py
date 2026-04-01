class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        for dy in range(-(n - 1), n):
            for dx in range(-(n - 1), n):
                current_overlap = 0
                for r1 in range(n):
                    for c1 in range(n):
                        if img1[r1][c1] == 1:
                            r2 = r1 + dy
                            c2 = c1 + dx
                            if 0 <= r2 < n and 0 <= c2 < n:
                                if img2[r2][c2] == 1:
                                    current_overlap += 1
                max_overlap = max(max_overlap, current_overlap)
        
        return max_overlap
