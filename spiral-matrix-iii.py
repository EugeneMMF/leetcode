class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        result = []
        visited = set()
        r, c = rStart, cStart

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        d = 0
        steps_taken_in_current_segment = 0
        current_segment_length = 1
        segments_completed_at_current_length = 0

        if 0 <= r < rows and 0 <= c < cols:
            result.append([r, c])
            visited.add((r, c))

        while len(result) < rows * cols:
            r += dr[d]
            c += dc[d]
            steps_taken_in_current_segment += 1

            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                result.append([r, c])
                visited.add((r, c))

            if steps_taken_in_current_segment == current_segment_length:
                d = (d + 1) % 4
                steps_taken_in_current_segment = 0
                segments_completed_at_current_length += 1
                if segments_completed_at_current_length == 2:
                    current_segment_length += 1
                    segments_completed_at_current_length = 0
        
        return result
