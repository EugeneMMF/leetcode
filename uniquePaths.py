class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    matrix = [[1]*n for _ in range(m)]
    if m == 1 or n == 1:
      return 1
    for i in reversed(list(range(m-1))):
      for j in reversed(list(range(n-1))):
        matrix[i][j] = matrix[i][j+1] + matrix[i+1][j]
    return matrix[0][0]

print(Solution().uniquePaths(1,100))