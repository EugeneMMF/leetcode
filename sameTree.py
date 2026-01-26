from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if (not p and q) or (not q and p): return False
    if not p and not q: return True
    nodesP = [p]
    nodesQ = [q]
    while nodesP and nodesQ:
      p, q = nodesP.pop(), nodesQ.pop()
      if p.val != q.val: return False
      if p.left and q.left:
        nodesP.append(p.left)
        nodesQ.append(q.left)
      elif p.left != q.left: return False
      if p.right and q.right:
        nodesP.append(p.right)
        nodesQ.append(q.right)
      elif p.right != q.right: return False
    if nodesP or nodesQ: return False
    return True