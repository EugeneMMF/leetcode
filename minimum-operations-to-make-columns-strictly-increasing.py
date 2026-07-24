class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        total = 0
        m = len(grid)
        n = len(grid[0]) if m else 0
        for j in range(n):
            prev = -1
            for i in range(m):
                val = grid[i][j]
                if val <= prev:
                    inc = prev + 1 - val
                    total += inc
                    val = prev + 1
                prev = val
        return total