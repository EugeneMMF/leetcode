from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            r, c = i, 0
            diag = []
            while r < m and c < n:
                diag.append(mat[r][c])
                r += 1
                c += 1
            diag.sort()
            r, c = i, 0
            idx = 0
            while r < m and c < n:
                mat[r][c] = diag[idx]
                idx += 1
                r += 1
                c += 1
        for j in range(1, n):
            r, c = 0, j
            diag = []
            while r < m and c < n:
                diag.append(mat[r][c])
                r += 1
                c += 1
            diag.sort()
            r, c = 0, j
            idx = 0
            while r < m and c < n:
                mat[r][c] = diag[idx]
                idx += 1
                r += 1
                c += 1
        return mat
