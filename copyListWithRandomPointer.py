from typing import Optional

# Definition for a Node.
class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random


class Solution:
  def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
    if not head: return None
    root = Node(head.val)
    mapping: dict[Node, Node] = {head: root}
    nodes = [head]
    while nodes:
      node = nodes.pop()
      mapping[node] = newNode = mapping.get(node, Node(node.val))
      if node.next:
        newNext = mapping.get(node.next, None)
        if not newNext:
          mapping[node.next] = newNext = Node(node.next.val)
          nodes.append(node.next)
        newNode.next = newNext
      if node.random:
        newRandom = mapping.get(node.random, None)
        if not newRandom:
          mapping[node.random] = newRandom = Node(node.random.val)
          nodes.append(node.random)
        newNode.random = newRandom
    return root