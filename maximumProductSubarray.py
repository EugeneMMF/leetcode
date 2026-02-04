from typing import List

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    l = len(nums)
    forward = [nums[0]]*l
    backward = [nums[-1]]*l
    for i in range(1,l):
      if forward[i-1] == 0:
        forward[i] = nums[i]
      else:
        forward[i] = forward[i-1] * nums[i]
    for i in range(l-2, -1, -1):
      if backward[i+1] == 0:
        backward[i] = nums[i]
      else:
        backward[i] = backward[i+1] * nums[i]
    return max(*forward, *backward)

print(Solution().maxProduct([2,-5,-2,-4,3]))