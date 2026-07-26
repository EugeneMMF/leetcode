class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        values = []
        for i in range(n):
            for v in grid[i]:
                values.append((v, i))
        values.sort(reverse=True, key=lambda x: x[0])
        taken = [0] * n
        count = 0
        total = 0
        for val, r in values:
            if count == k:
                break
            if taken[r] < limits[r]:
                taken[r] += 1
                count += 1
                total += val
        return total