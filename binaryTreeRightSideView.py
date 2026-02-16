from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    nodes = [root]
    values = []
    while nodes:
      tempNodes = nodes.copy()
      nodes = []
      lastValue = None
      for root in tempNodes:
        if root:
          nodes.append(root.left)
          nodes.append(root.right)
          lastValue = root.val
      if lastValue != None: values.append(lastValue)
    return values