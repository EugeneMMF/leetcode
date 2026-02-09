from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class BSTIterator:

  def __init__(self, root: Optional[TreeNode]):
    self.nodes = []
    def traverse(node):
      if not node: return
      traverse(node.right)
      self.nodes.append(node)
      traverse(node.left)
    traverse(root)

  def next(self) -> int:
    return self.nodes.pop().val

  def hasNext(self) -> bool:
    return len(self.nodes) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()