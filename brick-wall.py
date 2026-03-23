class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        edge_counts = {}
        n = len(wall)

        for row in wall:
            current_width = 0
            for brick_width in row[:-1]:
                current_width += brick_width
                edge_counts[current_width] = edge_counts.get(current_width, 0) + 1
        
        max_edges = 0
        if edge_counts:
            max_edges = max(edge_counts.values())
        
        return n - max_edges
