from typing import List

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    maxArea = 0
    states = [-1]
    heights += [0]
    for i,height in enumerate(heights):
      while heights[states[-1]] > height:
        maxArea = max(maxArea, heights[states.pop()] * (i - states[-1] - 1))
      states.append(i)
    return maxArea

print(Solution().largestRectangleArea([567,789]))