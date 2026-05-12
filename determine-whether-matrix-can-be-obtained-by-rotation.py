import typing

class Solution:
    def findRotation(self, mat: typing.List[typing.List[int]], target: typing.List[typing.List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            if mat == target:
                return True
            new_mat = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    new_mat[i][j] = mat[n-1-j][i]
            mat = new_mat
        return False
