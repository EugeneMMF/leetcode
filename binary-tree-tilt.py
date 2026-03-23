class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0

        def calculate_subtree_sum(node):
            if not node:
                return 0

            left_sum = calculate_subtree_sum(node.left)
            right_sum = calculate_subtree_sum(node.right)

            current_tilt = abs(left_sum - right_sum)
            self.total_tilt += current_tilt

            return node.val + left_sum + right_sum

        calculate_subtree_sum(root)
        return self.total_tilt
