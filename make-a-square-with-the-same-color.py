class Solution:
    def canMakeSquare(self, grid):
        for i in range(2):
            for j in range(2):
                sub = [grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
                b = sub.count('B')
                w = sub.count('W')
                if b >= 3 or w >= 3:
                    return True
        return False