from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        if not root:
            return root
        queue = deque([root])
        while queue:
            level_size = len(queue)
            nodes = []
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                parent = None
                if node is not root:
                    # find parent by checking children of nodes in previous level
                    # but easier: we can store parent when enqueuing children
                    pass
            # The above approach is complex; instead we store parent during enqueue
        # Revised approach with parent tracking
        queue = deque([(root, None)])
        while queue:
            level_size = len(queue)
            nodes = []
            level_sum = 0
            for _ in range(level_size):
                node, parent = queue.popleft()
                nodes.append((node, node.val, parent))
                level_sum += node.val
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            parent_sum = {}
            for node, val, parent in nodes:
                if parent not in parent_sum:
                    parent_sum[parent] = 0
                parent_sum[parent] += val
            for node, val, parent in nodes:
                node.val = level_sum - parent_sum[parent]
        return root
