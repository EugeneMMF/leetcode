from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    if len(nums) == 2:
      return max(nums[0], nums[1], sum(nums))
    leftSum = nums[0]
    maximum = max(nums[0], nums[-1])
    rightSum = nums[-1]
    l = 1
    r = len(nums) - 2
    while l <= r:
      if l != r:
        if nums[l] > 0:
          leftSum = max(leftSum, leftSum + nums[l], nums[l])
        else:
          if leftSum >= 0:
            leftSum = max(leftSum + nums[l], 0)
          else:
            leftSum = nums[l]
        if nums[r] > 0:
          rightSum = max(rightSum, rightSum + nums[r], nums[r])
        else:
          if leftSum >= 0:
            rightSum = max(rightSum + nums[r], 0)
          else:
            rightSum = nums[r]
        maximum = max(maximum, nums[r], nums[l], rightSum, leftSum)
      else:
        if maximum >= 0:
          maximum = max(maximum, leftSum + rightSum + nums[r], nums[r], leftSum + nums[r], rightSum + nums[r])
        else:
          maximum = max(maximum, leftSum, rightSum, nums[l])
        return maximum
      l += 1
      r -= 1
    maximum = max(maximum, leftSum, rightSum, leftSum+rightSum)
    return maximum