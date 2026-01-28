from typing import List

class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    l = len(triangle)
    if l == 1: return triangle[0][0]
    for i in reversed(range(l-1)):
      for j in range(i+1):
        triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))