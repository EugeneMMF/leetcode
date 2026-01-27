from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root: return False
    def helper(node, targetSum):
      if node.left:
        if node.right:
          return helper(node.left, targetSum-node.val) or helper(node.right, targetSum-node.val)
        return helper(node.left, targetSum-node.val)
      elif node.right:
        return helper(node.right, targetSum-node.val)
      return targetSum == node.val
    return helper(root, targetSum)