# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        if not root:
            return 0
        count = 0
        stack = [(root, root.val)]
        while stack:
            node, curmax = stack.pop()
            if node.val >= curmax:
                count += 1
                newmax = node.val
            else:
                newmax = curmax
            if node.right:
                stack.append((node.right, newmax))
            if node.left:
                stack.append((node.left, newmax))
        return count
