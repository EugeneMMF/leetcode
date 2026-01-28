from typing import Optional

# Definition for a Node.
class Node:
  def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next

class Solution:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if root is None: return root
    nodes = [root]
    while nodes:
      prev = nodes[0]
      if not prev: break
      tmp = [prev.left, prev.right]
      for node in nodes[1:]:
        tmp.append(node.left)
        tmp.append(node.right)
        prev.next = node
        prev = node
      nodes = tmp
    return root