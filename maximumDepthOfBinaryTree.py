from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
      if not root: return 0
      nodes = [(root, 1)]
      maxLevel = 0
      while nodes:
        node, level = nodes.pop()
        maxLevel = max(maxLevel, level)
        if node.right:
          nodes.append((node.right, level+1))
        if node.left:
          nodes.append((node.left, level+1))
      return maxLevel