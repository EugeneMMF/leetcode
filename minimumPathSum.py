from typing import List

class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    for i in reversed(list(range(m-1))):
      grid[i][n-1] += grid[i+1][n-1]
    for i in reversed(list(range(n-1))):
      grid[m-1][i] += grid[m-1][i+1]
    for i in reversed(list(range(m-1))):
      for j in reversed(list(range(n-1))):
        grid[i][j] += min(grid[i][j+1], grid[i+1][j])
    return grid[0][0]