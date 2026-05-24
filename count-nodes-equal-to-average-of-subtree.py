# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return 0, 0
            lsum, lcnt = dfs(node.left)
            rsum, rcnt = dfs(node.right)
            total = lsum + rsum + node.val
            totalcnt = lcnt + rcnt + 1
            if node.val == total // totalcnt:
                count += 1
            return total, totalcnt
        dfs(root)
        return count
