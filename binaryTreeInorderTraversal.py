from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root: return []
    solution = []
    nodes = [root]
    current = root
    while nodes:
      if not current:
        current = nodes.pop()
        solution.append(current.val)
        current = current.right
        if current:
          nodes.append(current)
        continue
      current = current.left
      if current:
        nodes.append(current)
    return solution