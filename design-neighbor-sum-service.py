 
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.position = {}
        for i in range(self.n):
            for j in range(self.n):
                self.position[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        x, y = self.position[value]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                total += self.grid[nx][ny]
        return total

    def diagonalSum(self, value: int) -> int:
        x, y = self.position[value]
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        total = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                total += self.grid[nx][ny]
        return total


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

