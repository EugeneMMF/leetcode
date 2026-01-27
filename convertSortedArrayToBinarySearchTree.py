from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def helper(start,end):
      if start == end: return None
      pivot = (start+end)//2
      root = TreeNode(nums[pivot])
      root.left = helper(start, pivot)
      root.right = helper(pivot+1, end)
      return root

    l = len(nums)
    return helper(0, l)