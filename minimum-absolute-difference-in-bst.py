class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        prev_val = None

        def inorder_traversal(node):
            nonlocal min_diff, prev_val
            if not node:
                return

            inorder_traversal(node.left)

            if prev_val is not None:
                min_diff = min(min_diff, abs(node.val - prev_val))
            prev_val = node.val

            inorder_traversal(node.right)

        inorder_traversal(root)
        return min_diff
