from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[TreeNode]:
    nodes = {i: TreeNode(i) for i in inOrder}
    l = len(preOrder)
    if l == 1: return nodes[preOrder[0]]
    def evaluate(i, currentList:list):
      try:
        cutPoint = currentList.index(preOrder[i])
      except:
        return evaluate(i+1, currentList)
      lefts,rights = currentList[:cutPoint], currentList[cutPoint+1:]
      if len(lefts) == 1:
        nodes[preOrder[i]].left = nodes[lefts[0]]
      elif len(lefts) > 1:
        nodes[preOrder[i]].left = evaluate(i+1, lefts)
      if len(rights) == 1:
        nodes[preOrder[i]].right = nodes[rights[0]]
      elif len(rights) > 1:
        nodes[preOrder[i]].right = evaluate(i+1, rights)
      return nodes[preOrder[i]]
    evaluate(0, inOrder)
    return nodes[preOrder[0]]

def traverseTree(root: TreeNode) -> tuple[int]:
  nodes = [root]
  vals = []
  while nodes:
    node = nodes.pop(0)
    if node:
      vals.append(node.val)
      nodes.append(node.left)
      nodes.append(node.right)
    else:
      vals.append(None)
  return tuple(vals)

print(traverseTree(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])))