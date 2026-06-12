class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        res = [0]*n
        for row in grid:
            for i, val in enumerate(row):
                length = len(str(abs(val))) + (1 if val < 0 else 0)
                if length > res[i]:
                    res[i] = length
        return res
