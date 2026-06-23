class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0]) if m else 0
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((mat[i][j], i, j))
        cells.sort()
        row_best = [0] * m
        col_best = [0] * n
        ans = 0
        idx = 0
        total = len(cells)
        while idx < total:
            val = cells[idx][0]
            group = []
            while idx < total and cells[idx][0] == val:
                _, i, j = cells[idx]
                dp = 1 + max(row_best[i], col_best[j])
                group.append((i, j, dp))
                if dp > ans:
                    ans = dp
                idx += 1
            for i, j, dp in group:
                if dp > row_best[i]:
                    row_best[i] = dp
                if dp > col_best[j]:
                    col_best[j] = dp
        return ans
