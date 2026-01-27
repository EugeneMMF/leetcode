from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if not root: return []
    def helper(node, targetSum):
      solutions = []
      if node.left:
        if tmp:=helper(node.left, targetSum-node.val):
          solutions.extend([[node.val]+i for i in tmp])
        if node.right:
          if tmp:=helper(node.right, targetSum-node.val):
            solutions.extend([[node.val]+i for i in tmp])
      elif node.right:
        if tmp:=helper(node.right, targetSum-node.val):
          solutions.extend([[node.val]+i for i in tmp])
      elif targetSum == node.val:
        return [[node.val]]
      return solutions
    return helper(root, targetSum)