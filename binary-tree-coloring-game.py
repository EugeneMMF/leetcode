# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int, color: str = "red") -> bool:
        
        def dfs(node, target_val):
            if not node:
                return None
            if node.val == target_val:
                return node
            left = dfs(node.left, target_val)
            if left:
                return left
            return dfs(node.right, target_val)

        target_node = dfs(root, x)

        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        left_subtree_size = count_nodes(target_node.left)
        right_subtree_size = count_nodes(target_node.right)
        parent_subtree_size = n - 1 - left_subtree_size - right_subtree_size

        half_n_plus_one = (n + 1) // 2

        if left_subtree_size >= half_n_plus_one:
            return True
        if right_subtree_size >= half_n_plus_one:
            return True
        if parent_subtree_size >= half_n_plus_one:
            return True

        return False

