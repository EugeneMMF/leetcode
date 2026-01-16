from typing import List

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    maxInd = 0
    n = len(nums)
    for i,num in enumerate(nums):
      if i > maxInd:
        return False
      tmp = num + i
      if maxInd < tmp:
        maxInd = tmp
      if maxInd >= n:
        return True
    return True