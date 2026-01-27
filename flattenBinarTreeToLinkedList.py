from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def flatten(self, root: Optional[TreeNode]) -> None:
    if not root: return
    nodes = [root]
    toJoin = False
    while nodes:
      if not toJoin:
        node = nodes.pop()
      else:
        node.right = nodes.pop()
        node = node.right
      toJoin = False
      if node.right:
        nodes.append(node.right)
      if node.left:
        node.right = node.left
        nodes.append(node.left)
        node.left = None
      if not node.right:
        toJoin = True