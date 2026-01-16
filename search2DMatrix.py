from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m,n = len(matrix), len(matrix[0])
    right = m*n-1
    left = 0
    while (right - left) > 1:
      center = int((left + right)/2)
      r = int(center/n)
      c = center%n
      if matrix[r][c] < target:
        left = center
      elif matrix[r][c] > target:
        right = center
      else:
        return True
    if (
      matrix[int(left/n)][left%n] == target or
      matrix[int(right/n)][right%n] == target
    ):
      return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(Solution().searchMatrix(matrix, 13))