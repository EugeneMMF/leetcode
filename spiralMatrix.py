from typing import List

class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    signRow = +1
    signCol = +1
    maxRow = len(matrix) - 1
    maxCol = len(matrix[0]) - 1
    minRow = 1
    minCol = 0
    passed = 0
    n = len(matrix) * len(matrix[0])
    r = c = 0
    solution = []
    horizontal = True
    while passed < n:
      pr = r
      pc = c
      solution.append(matrix[r][c])
      if c == maxCol and horizontal and signCol == 1:
        maxCol -= 1
        signCol = -1
        horizontal = False
      if r == maxRow and (not horizontal) and signRow == 1:
        maxRow -= 1
        signRow = -1
        horizontal = True
      if c == minCol and horizontal and signCol == -1:
        minCol += 1
        signCol = +1
        horizontal = False
      if r == minRow and (not horizontal) and signRow == -1:
        minRow += 1
        signRow = +1
        horizontal = True
      if horizontal:
        c += signCol
      else:
        r += signRow
      passed += 1
    return solution
