from typing import List

class Solution:
  def maximumGap(self, nums: List[int]) -> int:
    if len(nums) < 2: return 0
    nums.sort()
    maxDiff = 0
    for i in range(len(nums)-1):
      maxDiff = max(maxDiff, nums[i+1]-nums[i])
    return maxDiff