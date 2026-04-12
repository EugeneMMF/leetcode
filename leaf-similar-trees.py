from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect(node, out):
            if not node:
                return
            if not node.left and not node.right:
                out.append(node.val)
                return
            collect(node.left, out)
            collect(node.right, out)
        leaves1 = []
        collect(root1, leaves1)
        leaves2 = []
        collect(root2, leaves2)
        return leaves1 == leaves2
