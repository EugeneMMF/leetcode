from typing import Optional
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                v = node.val
                if level % 2 == 0:
                    if v % 2 == 0 or (prev is not None and v <= prev):
                        return False
                else:
                    if v % 2 == 1 or (prev is not None and v >= prev):
                        return False
                prev = v
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True
