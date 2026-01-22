from typing import Optional, List
from itertools import permutations

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    def traverseTree(root: TreeNode) -> tuple[int]:
      nodes = [root]
      vals = []
      while nodes:
        node = nodes.pop()
        vals.append(node.val)
        if node.right:
          nodes.append(node.right)
        else:
          pass
          # vals.append(None)
        if node.left:
          nodes.append(node.left)
        else:
          vals.append(None)
      return tuple(vals)

    def buildTree(vals: tuple[int]):
      vals = list(vals)
      root = TreeNode(vals.pop())
      while vals:
        node = root
        val = vals.pop()
        while node:
          if val < node.val:
            if node.left:
              node = node.left
            else:
              node.left = TreeNode(val)
              node = None
          elif node.right:
            node = node.right
          else:
            node.right = TreeNode(val)
            node = None
      return root

    solutions = []
    found = set()
    for vals in list(permutations(list(range(1, n+1)), n)):
      sol = buildTree(vals)
      traversal = traverseTree(sol)
      if traversal in found:
        continue
      found.add(traversal)
      solutions.append(sol)
    return solutions
  
print(len(Solution().generateTrees(5)))