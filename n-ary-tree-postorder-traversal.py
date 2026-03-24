# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.val)
            for child in node.children:
                stack.append(child)
        
        return output[::-1]
