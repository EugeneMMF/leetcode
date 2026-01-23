from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    lessGreater = [[],[]] # values less and values greater
    routes = []
    nodes = [root]
    while nodes:
      current = nodes.pop()
      if current.left:
        nodes.append(current)
        nodes.append(current.left)
        lessGreater[1].append(current.val)
        if current.left.val >= current.val: return False
        if len(lessGreater[0]) and lessGreater[0][-1] >= current.left.val: return False
        routes.append(1)
        current.left = None
        continue
      if current.right:
        nodes.append(current)
        nodes.append(current.right)
        lessGreater[0].append(current.val)
        if current.right.val <= current.val: return False
        if len(lessGreater[1]) and lessGreater[1][-1] <= current.right.val: return False
        routes.append(0)
        current.right = None
        continue
      if routes and lessGreater[routes[-1]]:
        lessGreater[routes.pop()].pop()
    return True

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
  print(Solution().isValidBST(buildTree((3,1,5,0,2,4,6,None,None,None,3))))