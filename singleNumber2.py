from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    seen = set()
    removed = set()
    for n in nums:
      if n in seen:
        removed.add(n)
      seen.add(n)
    return (seen - removed).pop()