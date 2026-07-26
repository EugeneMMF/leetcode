class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for d in range(-n + 1, n):
            vals = []
            if d >= 0:
                i = d
                j = 0
                while i < n and j < n:
                    vals.append(grid[i][j])
                    i += 1
                    j += 1
                vals.sort(reverse=True)
                i = d
                j = 0
                idx = 0
                while i < n and j < n:
                    grid[i][j] = vals[idx]
                    idx += 1
                    i += 1
                    j += 1
            else:
                i = 0
                j = -d
                while i < n and j < n:
                    vals.append(grid[i][j])
                    i += 1
                    j += 1
                vals.sort()
                i = 0
                j = -d
                idx = 0
                while i < n and j < n:
                    grid[i][j] = vals[idx]
                    idx += 1
                    i += 1
                    j += 1
        return grid
