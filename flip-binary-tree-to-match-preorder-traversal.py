# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root, voyage):
        self.idx = 0
        self.res = []
        def dfs(node):
            if not node:
                return True
            if self.idx >= len(voyage) or node.val != voyage[self.idx]:
                return False
            self.idx += 1
            if node.left and self.idx < len(voyage) and node.left.val != voyage[self.idx]:
                self.res.append(node.val)
                if not dfs(node.right):
                    return False
                if not dfs(node.left):
                    return False
            else:
                if not dfs(node.left):
                    return False
                if not dfs(node.right):
                    return False
            return True
        return self.res if dfs(root) else [-1]
