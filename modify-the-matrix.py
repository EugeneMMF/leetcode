import typing

class Solution:
    def modifiedMatrix(self, matrix: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]
        return matrix
