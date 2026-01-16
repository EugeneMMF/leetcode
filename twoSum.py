from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    mapping: dict[int, int] = {}
    for ind,num in enumerate(nums):
      remainder = target - num
      if (previous_index := mapping.get(num)) is not None:
        return [previous_index, ind]
      else:
        mapping[remainder] = ind