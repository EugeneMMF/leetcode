class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        rightmost = [ -1 ] * n
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    rightmost[i] = j
                    break
        swaps = 0
        for i in range(n):
            target = i
            j = i
            while j < n and rightmost[j] > target:
                j += 1
            if j == n:
                return -1
            while j > i:
                rightmost[j], rightmost[j-1] = rightmost[j-1], rightmost[j]
                swaps += 1
                j -= 1
        return swaps
