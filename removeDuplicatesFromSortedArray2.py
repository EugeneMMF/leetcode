from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 2: return n
    lookAt = 1
    placeAt = 1
    count = 1
    previous = nums[0]
    while lookAt < n:
      if nums[lookAt] == previous:
        if count < 2:
          nums[placeAt] = previous
          placeAt += 1
        count += 1
      else:
        count = 1
        previous = nums[lookAt]
        nums[placeAt] = previous
        placeAt += 1
      lookAt += 1
    return placeAt


class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    counts = {}
    array = []
    for num in nums:
      if (val:=counts.get(num, 0)) < 2:
        counts[num] = val + 1
        array.append(num)
    nums[:] = array