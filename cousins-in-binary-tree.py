# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x, y):
        from collections import deque
        q = deque([(root, None)])
        while q:
            size = len(q)
            x_parent = None
            y_parent = None
            for _ in range(size):
                node, parent = q.popleft()
                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            if x_parent is not None or y_parent is not None:
                return x_parent is not None and y_parent is not None and x_parent != y_parent
        return False
