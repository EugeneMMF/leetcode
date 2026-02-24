class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Calculate the x-overlap
        x_overlap_start = max(ax1, bx1)
        x_overlap_end = min(ax2, bx2)
        x_overlap_width = max(0, x_overlap_end - x_overlap_start)
        
        # Calculate the y-overlap
        y_overlap_start = max(ay1, by1)
        y_overlap_end = min(ay2, by2)
        y_overlap_height = max(0, y_overlap_end - y_overlap_start)
        
        intersection_area = x_overlap_width * y_overlap_height
        
        total_area = area_a + area_b - intersection_area
        
        return total_area
