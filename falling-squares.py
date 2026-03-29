class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        landed_squares = []
        ans = []
        max_overall_height = 0

        for left, side in positions:
            right = left + side
            current_square_bottom_y = 0

            for prev_left, prev_right, prev_height in landed_squares:
                if max(left, prev_left) < min(right, prev_right):
                    current_square_bottom_y = max(current_square_bottom_y, prev_height)
            
            new_square_top_y = current_square_bottom_y + side
            
            landed_squares.append((left, right, new_square_top_y))
            
            max_overall_height = max(max_overall_height, new_square_top_y)
            
            ans.append(max_overall_height)
            
        return ans
