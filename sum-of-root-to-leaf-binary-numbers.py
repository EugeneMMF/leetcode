class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def dfs(node, current_binary_value):
            nonlocal total_sum
            if not node:
                return

            current_binary_value = (current_binary_value << 1) | node.val

            if not node.left and not node.right:
                total_sum += current_binary_value
                return

            dfs(node.left, current_binary_value)
            dfs(node.right, current_binary_value)
        
        dfs(root, 0)
        return total_sum
