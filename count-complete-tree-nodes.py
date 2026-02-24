# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_depth_of_leftmost_path(node: Optional[TreeNode]) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        left_subtree_depth = get_depth_of_leftmost_path(root.left)
        right_subtree_depth = get_depth_of_leftmost_path(root.right)

        if left_subtree_depth == right_subtree_depth:
            # If the depths of the leftmost paths of the left and right subtrees are equal,
            # it implies that the entire tree rooted at 'root' is a perfect binary tree
            # of depth 'left_subtree_depth + 1'.
            # The number of nodes in a perfect binary tree of depth D is 2^D - 1.
            # Here, D = left_subtree_depth + 1.
            return (1 << (left_subtree_depth + 1)) - 1
        else: # left_subtree_depth must be equal to right_subtree_depth + 1 in a complete binary tree
            # This means the left subtree is a perfect binary tree of depth `left_subtree_depth`.
            # The total nodes are: 1 (for the root) + (nodes in the perfect left subtree) + (nodes in the right subtree).
            # Nodes in a perfect binary tree of depth D is 2^D - 1. Here D = left_subtree_depth.
            # So, 1 + ((1 << left_subtree_depth) - 1) + countNodes(root.right)
            # This simplifies to (1 << left_subtree_depth) + countNodes(root.right).
            return (1 << left_subtree_depth) + self.countNodes(root.right)

