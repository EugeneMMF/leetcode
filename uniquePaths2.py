from typing import List

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    matrix = [[1-x for x in row] for row in obstacleGrid]
    m = len(matrix)
    n = len(matrix[0])
    if m == 1:
      if not all(matrix[0]):
        return 0
      return 1
    if n == 1:
      if not all([matrix[i][0] for i in range(m)]):
        return 0
      return 1
    if matrix[m-1][n-1] == 0:
      return 0
    if not all(matrix[m-1]):
      for i in range(n - list(reversed(matrix[m-1])).index(0)):
        matrix[m-1][i] = 0
    tempMat = [matrix[i][n-1] for i in range(m)]
    if not all(tempMat):
      for i in range(m - list(reversed(tempMat)).index(0)):
        matrix[i][n-1] = 0
    for i in reversed(list(range(m-1))):
      for j in reversed(list(range(n-1))):
        if matrix[i][j] == 0:
          continue
        else:
          matrix[i][j] = matrix[i][j+1] + matrix[i+1][j]
    return matrix[0][0]

print(Solution().uniquePaths(1,100))