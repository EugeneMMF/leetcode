from typing import Optional

# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
    if not node: return node
    rootNode = Node(node.val)
    mapping: dict[Node, Node] = {node: rootNode}
    nodes: list[Node] = [node]
    addressed = set()
    while nodes:
      node = nodes.pop()
      addressed.add(node)
      newNode = mapping.get(node, Node(node.val))
      for neighbor in node.neighbors:
        newNeighbor = mapping.get(neighbor, Node(neighbor.val))
        newNode.neighbors.append(newNeighbor)
        if neighbor not in addressed:
          nodes.append(neighbor)
          addressed.add(neighbor)
        mapping[neighbor] = newNeighbor
      mapping[node] = newNode
    return rootNode