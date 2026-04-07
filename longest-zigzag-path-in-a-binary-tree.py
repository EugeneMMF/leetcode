# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        max_zigzag_length = 0

        def dfs(node):
            nonlocal max_zigzag_length
            if not node:
                return -1, -1

            left_res_left, left_res_right = dfs(node.left)
            right_res_left, right_res_right = dfs(node.right)

            current_left_zigzag_len = 1 + left_res_right
            current_right_zigzag_len = 1 + right_res_left

            max_zigzag_length = max(max_zigzag_length, current_left_zigzag_len, current_right_zigzag_len)

            return current_left_zigzag_len, current_right_zigzag_len

        dfs(root)
        return max_zigzag_length
