class Solution:
    def largest1BorderedSquare(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        right = [[0] * cols for _ in range(rows)]
        down = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols - 1, -1, -1):
                if grid[r][c] == 1:
                    right[r][c] = (right[r][c+1] if c + 1 < cols else 0) + 1
        
        for c in range(cols):
            for r in range(rows - 1, -1, -1):
                if grid[r][c] == 1:
                    down[r][c] = (down[r+1][c] if r + 1 < rows else 0) + 1
        
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for side in range(min(right[r][c], down[r][c]), 0, -1):
                        if (r + side - 1 < rows and
                            c + side - 1 < cols and
                            right[r + side - 1][c] >= side and
                            down[r][c + side - 1] >= side):
                            max_side = max(max_side, side)
                            break
        
        return max_side * max_side
