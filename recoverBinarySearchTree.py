from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> bool:
    def verifySub(node):
      if node is None: return
      verifySub(node.left)
      nonlocal prev,first,second
      if prev and prev.val > node.val:
        if first is None:
          first = prev
        second = node
      prev = node
      verifySub(node.right)

    prev = first = second = None
    verifySub(root)
    first.val, second.val = second.val, first.val
    return root

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
  val = vals[0]
  root = TreeNode(val)
  node = root
  i = 1
  nodes = {val: root}
  for s in range(1, len(vals)-1, 2):
    if vals[s]:
      nodes[vals[s]] = node.left = TreeNode(vals[s])
    if vals[s+1]:
      nodes[vals[s+1]] = node.right = TreeNode(vals[s+1])
    if vals[i]:
      node = nodes[vals[i]]
    i+=1
  return root

if __name__ == "__main__":
  print(traverseTree(Solution().recoverTree(buildTree((1,3,None,None,2)))))