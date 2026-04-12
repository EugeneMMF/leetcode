# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def dfs(node, par):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)
        q = deque()
        visited = set()
        q.append((target, 0))
        visited.add(target)
        res = []
        while q:
            node, d = q.popleft()
            if d == k:
                res.append(node.val)
            if d < k:
                for nb in (node.left, node.right, parent.get(node)):
                    if nb and nb not in visited:
                        visited.add(nb)
                        q.append((nb, d + 1))
        return res
