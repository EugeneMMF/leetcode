from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 1: return nums[0]
    rob1, rob2 = 0, 0
    for num in nums[:-1]:
      rob1, rob2 = rob2, max(rob1+num, rob2)
    robMax = rob2
    rob1, rob2 = 0, 0
    for num in nums[1:]:
      rob1, rob2 = rob2, max(rob1+num, rob2)
    return max(robMax, rob2)