from typing import List

class Solution:
  def jump(self, nums: List[int]) -> int:
    n = len(nums)
    i = 0
    count = 0
    if n == 1:
      return 0
    while i < n-1:
      count += 1
      if i + nums[i] + 1 >= n:
        break
      next_biggest_ind = 0
      ind = i
      for j in range(1, min(nums[i]+1, n-i)):
        if i+j+nums[i+j] > next_biggest_ind:
          next_biggest_ind = i+j+nums[i+j]
          ind = i + j
      i = ind
    return count