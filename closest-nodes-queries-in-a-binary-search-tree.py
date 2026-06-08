from typing import List, Optional
import bisect

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            vals.append(node.val)
            node = node.right
        res = []
        for q in queries:
            i = bisect.bisect_left(vals, q)
            if i < len(vals) and vals[i] == q:
                floor = vals[i]
            else:
                floor = vals[i-1] if i > 0 else -1
            ceil = vals[i] if i < len(vals) else -1
            res.append([floor, ceil])
        return res