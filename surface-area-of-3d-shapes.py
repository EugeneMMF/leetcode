class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        total_surface_area = 0

        for r in range(N):
            for c in range(N):
                current_height = grid[r][c]

                if current_height == 0:
                    continue

                # Add top and bottom faces for the current tower of cubes
                total_surface_area += 2

                # Calculate exposed vertical faces by comparing with neighbors
                # For each direction, if current_height is greater than neighbor's height,
                # the difference contributes to the surface area.
                # If a neighbor is out of bounds, treat its height as 0.

                # Check North neighbor (r-1, c)
                neighbor_height_north = 0
                if r > 0:
                    neighbor_height_north = grid[r-1][c]
                total_surface_area += max(0, current_height - neighbor_height_north)

                # Check South neighbor (r+1, c)
                neighbor_height_south = 0
                if r < N - 1:
                    neighbor_height_south = grid[r+1][c]
                total_surface_area += max(0, current_height - neighbor_height_south)

                # Check West neighbor (r, c-1)
                neighbor_height_west = 0
                if c > 0:
                    neighbor_height_west = grid[r][c-1]
                total_surface_area += max(0, current_height - neighbor_height_west)

                # Check East neighbor (r, c+1)
                neighbor_height_east = 0
                if c < N - 1:
                    neighbor_height_east = grid[r][c+1]
                total_surface_area += max(0, current_height - neighbor_height_east)
        
        return total_surface_area
