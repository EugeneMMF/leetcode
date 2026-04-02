class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        xy_area = 0
        zx_area = 0
        yz_area = 0
        
        col_maxes = [0] * n
        
        for i in range(n):
            row_max = 0
            for j in range(n):
                height = grid[i][j]
                
                if height > 0:
                    xy_area += 1
                
                row_max = max(row_max, height)
                col_maxes[j] = max(col_maxes[j], height)
            
            zx_area += row_max
            
        yz_area = sum(col_maxes)
        
        return xy_area + zx_area + yz_area
