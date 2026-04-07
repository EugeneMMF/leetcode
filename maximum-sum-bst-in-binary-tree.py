from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        max_sum_so_far = 0

        def dfs(node):
            nonlocal max_sum_so_far

            if not node:
                return True, float('inf'), float('-inf'), 0

            left_is_bst, left_min, left_max, left_sum = dfs(node.left)
            right_is_bst, right_min, right_max, right_sum = dfs(node.right)

            if left_is_bst and right_is_bst and node.val > left_max and node.val < right_min:
                current_total_sum = left_sum + right_sum + node.val
                max_sum_so_far = max(max_sum_so_far, current_total_sum)
                
                return True, min(left_min, node.val), max(right_max, node.val), current_total_sum
            else:
                return False, float('-inf'), float('inf'), 0

        dfs(root)
        return max_sum_so_far
