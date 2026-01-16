from typing import List
from itertools import permutations

class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    return [list(item) for item in set(permutations(nums))]