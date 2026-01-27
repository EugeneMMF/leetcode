from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    nodes = [root]
    i = 0
    while True:
      tmp = []
      for node in nodes:
        if not node.left:
          if not node.right:
            return i
          tmp.append(node.right)
        else:
          tmp.append(node.left)
          if node.right:
            tmp.append(node.right)
      i += 1
      nodes = tmp