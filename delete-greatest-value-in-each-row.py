class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in grid:
            row.sort()
        ans = 0
        for _ in range(n):
            max_deleted = 0
            for row in grid:
                val = row.pop()
                if val > max_deleted:
                    max_deleted = val
            ans += max_deleted
        return ans
