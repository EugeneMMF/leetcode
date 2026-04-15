# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root):
        self.best = None
        def dfs(node, path):
            if not node:
                return
            path.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                cand = ''.join(reversed(path))
                if self.best is None or cand < self.best:
                    self.best = cand
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return self.best
