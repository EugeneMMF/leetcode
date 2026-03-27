class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        landed_squares = []
        ans = []
        current_overall_max_height = 0

        for left, side in positions:
            right = left + side
            
            current_square_base_y = 0 
            
            for prev_left, prev_right, prev_height in landed_squares:
                if max(left, prev_left) < min(right, prev_right):
                    current_square_base_y = max(current_square_base_y, prev_height)
            
            current_square_top_y = current_square_base_y + side
            
            landed_squares.append((left, right, current_square_top_y))
            
            current_overall_max_height = max(current_overall_max_height, current_square_top_y)
            
            ans.append(current_overall_max_height)
            
        return ans
