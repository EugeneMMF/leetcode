# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import typing
class Solution:
    def reverseOddLevels(self, root: typing.Optional[TreeNode]) -> typing.Optional[TreeNode]:
        def dfs(n1, n2, level):
            if not n1 or not n2:
                return
            if level % 2 == 1:
                n1.val, n2.val = n2.val, n1.val
            dfs(n1.left, n2.right, level+1)
            dfs(n1.right, n2.left, level+1)
        if root:
            dfs(root.left, root.right, 1)
        return root
