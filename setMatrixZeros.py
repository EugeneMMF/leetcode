from typing import List

class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    rows = set()
    cols = set()
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          rows.add(i)
          cols.add(j)
    for i in rows:
      matrix[i] = [0]*n
    for j in cols:
      for i in range(m):
        matrix[i][j] = 0