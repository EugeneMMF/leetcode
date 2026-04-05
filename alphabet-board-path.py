class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        char_coords = {}
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for r, row_str in enumerate(board):
            for c, char_val in enumerate(row_str):
                char_coords[char_val] = (r, c)

        curr_r, curr_c = 0, 0
        result = []

        for char_code in target:
            target_r, target_c = char_coords[char_code]

            row_diff = target_r - curr_r
            col_diff = target_c - curr_c
            
            if curr_r == 5 and curr_c == 0: # Moving from 'z'
                # Prioritize 'U' to escape row 5
                if row_diff < 0:
                    result.append('U' * abs(row_diff))
                # Then horizontal moves
                if col_diff < 0:
                    result.append('L' * abs(col_diff))
                if col_diff > 0:
                    result.append('R' * col_diff)
            elif target_r == 5 and target_c == 0: # Moving to 'z'
                # Prioritize horizontal moves to reach column 0 first
                if col_diff < 0:
                    result.append('L' * abs(col_diff))
                if col_diff > 0:
                    result.append('R' * col_diff)
                # Then 'D' to reach row 5
                if row_diff > 0:
                    result.append('D' * row_diff)
            else: # General case (neither current nor target involves special 'z' interactions)
                # Standard order: vertical moves then horizontal moves
                if row_diff < 0:
                    result.append('U' * abs(row_diff))
                if row_diff > 0:
                    result.append('D' * row_diff)
                if col_diff < 0:
                    result.append('L' * abs(col_diff))
                if col_diff > 0:
                    result.append('R' * col_diff)

            result.append('!')
            curr_r, curr_c = target_r, target_c
        
        return "".join(result)

