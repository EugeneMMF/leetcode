class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]

            max_len = 1

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
            
            memo[r][c] = max_len
            return max_len

        overall_max_path = 0
        for r in range(m):
            for c in range(n):
                overall_max_path = max(overall_max_path, dfs(r, c))
        
        return overall_max_path
