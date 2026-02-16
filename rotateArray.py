from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    if k == 0: return
    nums[:] = nums[-k:] + nums[:len(nums)-k]