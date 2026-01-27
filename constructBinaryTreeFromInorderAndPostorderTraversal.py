from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def buildTree(self, inOrder: List[int], postOrder: List[int]) -> Optional[TreeNode]:
    # First create all the nodes
    nodes = {i: TreeNode(i) for i in inOrder}
    indexes = {val:i for i,val in enumerate(inOrder)}
    l = len(inOrder)
    # If there is only one node, return it
    if l == 1: return nodes[inOrder[0]]

    def link(i: int, start: int, end: int) -> TreeNode|None:
      if i < 0: return None
      pivot = indexes[postOrder[i]]
      if pivot < start or pivot > end:
        return link(i-1, start, end)
      if end-pivot == 2:
        nodes[postOrder[i]].right = nodes[inOrder[pivot+1]]
      elif end-pivot > 2:
        nodes[postOrder[i]].right = link(i-1, pivot+1, end)
      if pivot-start == 1:
        nodes[postOrder[i]].left = nodes[inOrder[start]]
      elif pivot-start > 1:
        nodes[postOrder[i]].left = link(i-1, start, pivot)
      return nodes[postOrder[i]]

    link(l-1, 0, l)
    return nodes[postOrder[l-1]]

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

print(traverseTree(Solution().buildTree([1,2,3,4],[2,1,4,3])))