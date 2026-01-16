from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    res = []
    increment = 1
    for i in reversed(digits):
      res.append((i + increment)%10)
      increment = int((i+increment)/10)
    if increment:
      res.append(increment)
    return list(reversed(res))