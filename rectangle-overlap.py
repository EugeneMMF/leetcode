class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1_rec1, y1_rec1, x2_rec1, y2_rec1 = rec1
        x1_rec2, y1_rec2, x2_rec2, y2_rec2 = rec2

        x_overlap = max(x1_rec1, x1_rec2) < min(x2_rec1, x2_rec2)
        y_overlap = max(y1_rec1, y1_rec2) < min(y2_rec1, y2_rec2)

        return x_overlap and y_overlap
