import random

class Solution:

    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.cumulative_points = []
        total_points = 0
        for x1, y1, x2, y2 in rects:
            num_points_in_rect = (x2 - x1 + 1) * (y2 - y1 + 1)
            total_points += num_points_in_rect
            self.cumulative_points.append(total_points)
        self.total_points = total_points

    def pick(self) -> list[int]:
        target_point_index = random.randint(1, self.total_points)

        chosen_rect_idx = 0
        for i, cumulative_sum in enumerate(self.cumulative_points):
            if target_point_index <= cumulative_sum:
                chosen_rect_idx = i
                break
        
        x1, y1, x2, y2 = self.rects[chosen_rect_idx]
        
        rand_x = random.randint(x1, x2)
        rand_y = random.randint(y1, y2)
        
        return [rand_x, rand_y]
