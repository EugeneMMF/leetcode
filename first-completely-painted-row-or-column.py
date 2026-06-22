class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        pos = {}
        for r in range(m):
            for c in range(n):
                pos[mat[r][c]] = (r, c)
        row_counts = [0] * m
        col_counts = [0] * n
        for i, v in enumerate(arr):
            r, c = pos[v]
            row_counts[r] += 1
            if row_counts[r] == n:
                return i
            col_counts[c] += 1
            if col_counts[c] == m:
                return i
        return -1