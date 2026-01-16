from typing import List

class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    nums = sorted(set(nums))
    min = 1
    for num in nums:
      if num > 0:
        if min == num:
          min += 1
        elif min < num:
          break
    return min