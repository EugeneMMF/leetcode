class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        center = n // 2
        len_diag = center + 1
        totalY = 3 * len_diag - 1
        totalOut = n * n - totalY
        freqY = [0, 0, 0]
        freqOut = [0, 0, 0]
        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                if (r == c and r <= center) or (r + c == n - 1 and r <= center) or (c == center and r >= center):
                    freqY[val] += 1
                else:
                    freqOut[val] += 1
        min_ops = n * n
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                ops = (totalY - freqY[a]) + (totalOut - freqOut[b])
                if ops < min_ops:
                    min_ops = ops
        return min_ops