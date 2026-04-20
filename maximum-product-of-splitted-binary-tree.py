class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.total = 0
        def dfs_total(node):
            if not node:
                return 0
            s = node.val + dfs_total(node.left) + dfs_total(node.right)
            self.total += node.val
            return s
        dfs_total(root)
        self.max_prod = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node.val + left + right
            self.max_prod = max(self.max_prod, cur * (self.total - cur))
            return cur
        dfs(root)
        return self.max_prod % MOD
