from typing import List
from itertools import permutations

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    # result = []
    # if len(nums) == 1:
    #   return [nums]
    # for i in range(len(nums)):
    #   temp = nums[0:i] + nums[i+1:]
    #   temps = self.permute(temp)
    #   for t in temps:
    #     result.append([nums[i], *t])
    # return result
    return [list(item) for item in permutations(nums)]