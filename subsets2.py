from typing import List
from itertools import combinations

class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    results = set()
    for i in range(len(nums)+1):
      combs = set([tuple(sorted(t)) for t in list(combinations(nums, i))])
      results = results.union(combs)
    return list(results)