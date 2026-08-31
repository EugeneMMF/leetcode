from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Wrapper:
    def __init__(self, node):
        self.node = node
        self.seen = False

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        newRoot = Wrapper(root)
        nodes = [newRoot]
        sum = 0
        while nodes:
            node = nodes.pop()
            if node.seen:
                temp = node.node.val
                node.node.val += sum
                sum += temp
                continue
            if node.node.left:
                nodes.append(Wrapper(node.node.left))
            nodes.append(node)
            if node.node.right:
                nodes.append(Wrapper(node.node.right))
            node.seen = True
        return root