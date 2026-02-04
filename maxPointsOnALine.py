from typing import List

class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    gradients = {tuple(point): {} for point in points}
    maxPoints = 1
    for point in points:
      p1 = tuple(point)
      for p in points:
        p2 = tuple(p)
        if p1 == p2: continue
        if (p2[0] - p1[0]) == 0:
          grad = "inf"
        else:
          grad = (p2[1] - p1[1])/(p2[0] - p1[0])
        gradients[p1][grad] = t = gradients[p1].get(grad, 1) + 1
        maxPoints = max(maxPoints, t)
    return maxPoints