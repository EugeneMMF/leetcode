from typing import List

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.grid = grid
        self.pos = {}
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                self.pos[val] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.pos[value]
        s = 0
        if i > 0:
            s += self.grid[i - 1][j]
        if i < self.n - 1:
            s += self.grid[i + 1][j]
        if j > 0:
            s += self.grid[i][j - 1]
        if j < self.n - 1:
            s += self.grid[i][j + 1]
        return s

    def diagonalSum(self, value: int) -> int:
        i, j = self.pos[value]
        s = 0
        if i > 0 and j > 0:
            s += self.grid[i - 1][j - 1]
        if i > 0 and j < self.n - 1:
            s += self.grid[i - 1][j + 1]
        if i < self.n - 1 and j > 0:
            s += self.grid[i + 1][j - 1]
        if i < self.n - 1 and j < self.n - 1:
            s += self.grid[i + 1][j + 1]
        return s

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
