from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    values = {}
    for i,num in enumerate(numbers):
      key = target - num
      if key in values:
        return [values[key] + 1, i + 1]
      values[num] = values.get(num, i)