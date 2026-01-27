from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def balanced(node):
      if not node: return 1
      left = balanced(node.left)
      right = balanced(node.right)
      if right == False or left == False: return False
      if abs(left - right) > 1:
        return False
      return max(left+1, right+1)
    if balanced(root) != False:
      return True
    return False