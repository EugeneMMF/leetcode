from typing import List

class Solution:
  def largestRectangleArea(self, matrix: List[int]) -> int:
    n = len(matrix[0])
    heights = [0]*(n+1)
    maxArea = 0
    for row in matrix:
      for i in range(n):
        height[i] = height[i] + 1 if row[i] == "1" else 0
      states = [-1]
      for i,height in enumerate(heights):
        while heights[states[-1]] > height:
          maxArea = max(maxArea, heights[states.pop()] * (i - states[-1] - 1))
        states.append(i)
    return maxArea