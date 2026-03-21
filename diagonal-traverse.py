class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])

        result = []
        row, col = 0, 0
        up_direction = True

        for _ in range(m * n):
            result.append(mat[row][col])

            if up_direction:
                next_row, next_col = row - 1, col + 1

                if next_col >= n:
                    row += 1
                    up_direction = False
                elif next_row < 0:
                    col += 1
                    up_direction = False
                else:
                    row = next_row
                    col = next_col
            else:
                next_row, next_col = row + 1, col - 1

                if next_row >= m:
                    col += 1
                    up_direction = True
                elif next_col < 0:
                    row += 1
                    up_direction = True
                else:
                    row = next_row
                    col = next_col
        
        return result
