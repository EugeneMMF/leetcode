from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        target = set(range(1, n + 1))
        for row in matrix:
            if set(row) != target:
                return False
        for c in range(n):
            col = {matrix[r][c] for r in range(n)}
            if col != target:
                return False
        return True
