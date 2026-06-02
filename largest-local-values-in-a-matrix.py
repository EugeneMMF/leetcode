class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                mx = 0
                for di in range(3):
                    for dj in range(3):
                        val = grid[i + di][j + dj]
                        if val > mx:
                            mx = val
                res[i][j] = mx
        return res
