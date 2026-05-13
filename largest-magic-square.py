class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_k = min(m, n)
        for k in range(max_k, 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    target = sum(grid[r][c + i] for i in range(k))
                    ok = True
                    for i in range(k):
                        if sum(grid[r + i][c + j] for j in range(k)) != target:
                            ok = False
                            break
                    if not ok:
                        continue
                    for j in range(k):
                        if sum(grid[r + i][c + j] for i in range(k)) != target:
                            ok = False
                            break
                    if not ok:
                        continue
                    if sum(grid[r + i][c + i] for i in range(k)) != target:
                        continue
                    if sum(grid[r + i][c + k - 1 - i] for i in range(k)) != target:
                        continue
                    return k
        return 1
