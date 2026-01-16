from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    water = 0
    maxLefts = [height[0]]
    tmp = list(enumerate(height))
    maxRights = [height[-1]]
    currentMax = height[0]
    for i,h in tmp[1:]:
      maxLefts.append(currentMax)
      currentMax = max(currentMax, h)
    currentMax = height[-1]
    tmp.reverse()
    for i,h in tmp[1:]:
      maxRights.append(currentMax)
      currentMax = max(currentMax, h)
    maxRights.reverse()
    for i,h in enumerate(height):
      if (temp:=min(maxLefts[i], maxRights[i]) - h) > 0:
        water += temp
    return water