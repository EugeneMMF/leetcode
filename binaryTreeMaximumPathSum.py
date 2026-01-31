from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    maximum = root.val
    def helper(node):
      nonlocal maximum
      if not node: return 0
      left = helper(node.left)
      right = helper(node.right)
      ln = left + node.val
      rn = right + node.val
      t = max(ln, rn, node.val)
      maximum = max(t, ln + right, maximum)
      return t
    t = helper(root)
    return max(maximum, t)