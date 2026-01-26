from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    lefts = []
    rights = []
    if root.left and root.right:
      lefts.append(root.left)
      rights.append(root.right)
    elif root.left != root.right:
      return False
    while lefts and rights:
      l,r = lefts.pop(), rights.pop()
      if l.val != r.val: return False
      if l.left and r.right:
        lefts.append(l.left)
        rights.append(r.right)
      elif l.left != r.right: return False
      if l.right and r.left:
        lefts.append(l.right)
        rights.append(r.left)
      elif l.right != r.left: return False
    if lefts or rights: return False
    return True