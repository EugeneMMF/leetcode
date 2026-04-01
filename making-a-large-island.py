class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_id_counter = 2
        island_sizes = {}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    current_size = 0
                    stack = [(r, c)]
                    grid[r][c] = island_id_counter
                    current_size += 1

                    while stack:
                        curr_r, curr_c = stack.pop()
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = island_id_counter
                                current_size += 1
                                stack.append((nr, nc))
                    
                    island_sizes[island_id_counter] = current_size
                    island_id_counter += 1
        
        max_overall_size = max(island_sizes.values()) if island_sizes else 0

        found_zero = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    found_zero = True
                    neighbor_islands = set()
                    
                    current_potential_size = 1 
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] >= 2:
                            neighbor_islands.add(grid[nr][nc])
                    
                    for island_id in neighbor_islands:
                        current_potential_size += island_sizes[island_id]
                    
                    max_overall_size = max(max_overall_size, current_potential_size)
        
        if not found_zero:
            return n * n 
        
        return max_overall_size
