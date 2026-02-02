from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    total = 0
    nodes = [(0,root)]
    while nodes:
      val,node = nodes.pop()
      val = val*10 + node.val
      if node.left:
        nodes.append((val,node.left))
        if node.right:
          nodes.append((val,node.right))
      elif node.right:
        nodes.append((val,node.right))
      else:
        total += val
    return total