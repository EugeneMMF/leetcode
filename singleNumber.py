from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    rem = 0
    for num in nums:
      rem ^= num
    return rem