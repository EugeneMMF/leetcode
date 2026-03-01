class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        
        # Create a (m+1) x (n+1) prefix sum matrix, initialized to zeros.
        # dp[i][j] stores the sum of elements in the rectangle from (0,0) to (i-1, j-1)
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for r in range(m):
            for c in range(n):
                # Calculate the sum for the rectangle ending at (r, c)
                # using the formula:
                # current_sum = element_at_matrix[r][c] + sum_above + sum_left - sum_diagonal_overlap
                self.dp[r + 1][c + 1] = matrix[r][c] + self.dp[r][c + 1] + self.dp[r + 1][c] - self.dp[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # The sum of the rectangle (row1, col1) to (row2, col2) can be found using:
        # dp[row2+1][col2+1] (sum of rectangle from (0,0) to (row2, col2))
        # - dp[row1][col2+1] (subtract sum of rectangle from (0,0) to (row1-1, col2))
        # - dp[row2+1][col1] (subtract sum of rectangle from (0,0) to (row2, col1-1))
        # + dp[row1][col1]   (add back sum of rectangle from (0,0) to (row1-1, col1-1) which was subtracted twice)
        
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
