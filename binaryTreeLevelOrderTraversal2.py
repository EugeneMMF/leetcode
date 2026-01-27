from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root: return []
      solutions = {}
      nodes = [(root, 0)]
      maxLevel = 0
      while nodes:
        node, level = nodes.pop()
        solutions[level] = solutions.get(level, []) + [node.val]
        maxLevel = max(maxLevel, level)
        if node.right:
          nodes.append((node.right, level+1))
        if node.left:
          nodes.append((node.left, level+1))
      finalSolution = []
      for i in range(maxLevel,-1,-1):
        finalSolution.append(solutions.get(i, []))
      return finalSolution