class Solution:
    def sufficientSubset(self, root, limit):
        def maxDown(node):
            if not node:
                return -10**18
            left = maxDown(node.left)
            right = maxDown(node.right)
            if node.left is None and node.right is None:
                return node.val
            return node.val + (left if left > right else right)
        memo = {}
        def compute(node):
            if not node:
                return -10**18
            if node in memo:
                return memo[node]
            if node.left is None and node.right is None:
                memo[node] = node.val
                return node.val
            left = compute(node.left)
            right = compute(node.right)
            memo[node] = node.val + (left if left > right else right)
            return memo[node]
        compute(root)
        def dfs(node, acc):
            if not node:
                return None
            if acc + memo[node] < limit:
                return None
            node.left = dfs(node.left, acc + node.val)
            node.right = dfs(node.right, acc + node.val)
            return node
        return dfs(root, 0)
