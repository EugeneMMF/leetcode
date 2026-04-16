# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):
        total = 0
        def traverse(node):
            nonlocal total
            if not node:
                return
            traverse(node.right)
            total += node.val
            node.val = total
            traverse(node.left)
        traverse(root)
        return root
