class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        
        flat_grid = []
        for r in range(m):
            for c in range(n):
                flat_grid.append(grid[r][c])
        
        total_elements = m * n
        
        k_eff = k % total_elements
        
        shifted_flat_grid = flat_grid[-k_eff:] + flat_grid[:-k_eff]
        
        result_grid = []
        for r in range(m):
            row = []
            for c in range(n):
                current_flat_idx = r * n + c
                row.append(shifted_flat_grid[current_flat_idx])
            result_grid.append(row)
            
        return result_grid

