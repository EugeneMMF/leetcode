from typing import List

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    counts = {0: 0, 1: 0, 2: 0}
    for i in nums:
      counts[i] += 1
    for i,n in enumerate([0]*counts[0] + [1]*counts[1] + [2]*counts[2]):
      nums[i] = n