class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0, None

            depth_l, lca_l = dfs(node.left)
            depth_r, lca_r = dfs(node.right)

            if depth_l == depth_r:
                return 1 + depth_l, node
            elif depth_l > depth_r:
                return 1 + depth_l, lca_l
            else:
                return 1 + depth_r, lca_r

        _, result_lca = dfs(root)
        return result_lca
