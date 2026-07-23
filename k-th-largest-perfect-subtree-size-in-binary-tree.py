# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []
        def dfs(node):
            if not node:
                return False, 0, -1
            if not node.left and not node.right:
                sizes.append(1)
                return True, 1, 0
            left_perfect, left_size, left_height = dfs(node.left)
            right_perfect, right_size, right_height = dfs(node.right)
            if left_perfect and right_perfect and left_height == right_height:
                size = left_size + right_size + 1
                height = left_height + 1
                sizes.append(size)
                return True, size, height
            return False, 0, 0
        dfs(root)
        if len(sizes) < k:
            return -1
        sizes.sort(reverse=True)
        return sizes[k-1]
