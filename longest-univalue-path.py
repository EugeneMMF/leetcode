class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node):
            if not node:
                return 0

            left_path_len = dfs(node.left)
            right_path_len = dfs(node.right)

            current_left_extension = 0
            current_right_extension = 0

            if node.left and node.left.val == node.val:
                current_left_extension = 1 + left_path_len
            
            if node.right and node.right.val == node.val:
                current_right_extension = 1 + right_path_len
            
            self.max_len = max(self.max_len, current_left_extension + current_right_extension)

            return max(current_left_extension, current_right_extension)

        dfs(root)
        return self.max_len
