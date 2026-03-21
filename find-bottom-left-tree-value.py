
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = collections.deque([root])
        last_row_leftmost_val = 0

        while q:
            level_size = len(q)
            last_row_leftmost_val = q[0].val 

            for _ in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return last_row_leftmost_val
