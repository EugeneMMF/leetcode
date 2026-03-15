import collections

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        result = []
        if not root:
            return result

        queue = collections.deque([root])

        while queue:
            current_level_nodes = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                current_level_nodes.append(node.val)
                for child in node.children:
                    queue.append(child)
            
            result.append(current_level_nodes)
            
        return result
