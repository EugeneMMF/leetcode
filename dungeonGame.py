from typing import List

class Solution:
  def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    m,n = len(dungeon), len(dungeon[0])
    values = [[0]*n for _ in range(m)]
    mm,nn = m-1, n-1
    values[mm][nn] = 1 if dungeon[mm][nn] >= 0 else 1-dungeon[mm][nn]
    for i in range(mm-1, -1, -1):
      if dungeon[i][nn] >= values[i+1][nn]:
        values[i][nn] = 1
      else:
        values[i][nn] = values[i+1][nn] - dungeon[i][nn]
    for i in range(nn-1, -1, -1):
      if dungeon[mm][i] >= values[mm][i+1]:
        values[mm][i] = 1
      else:
        values[mm][i] = values[mm][i+1] - dungeon[mm][i]
    for i in range(mm-1, -1, -1):
      for j in range(nn-1, -1, -1):
        cost = min(values[i][j+1], values[i+1][j])
        if dungeon[i][j] >= cost:
          values[i][j] = 1
        else:
          values[i][j] = cost - dungeon[i][j]
    return values[0][0]