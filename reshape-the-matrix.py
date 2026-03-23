class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        new_mat = []
        for _ in range(r):
            new_mat.append([0] * c)

        element_index = 0
        for i in range(m):
            for j in range(n):
                new_row = element_index // c
                new_col = element_index % c
                new_mat[new_row][new_col] = mat[i][j]
                element_index += 1
        
        return new_mat
