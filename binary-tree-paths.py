# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        paths = []

        def dfs(node, current_path):
            if not node:
                return

            current_path.append(str(node.val))

            if not node.left and not node.right:
                paths.append("->".join(current_path))
            else:
                dfs(node.left, current_path)
                dfs(node.right, current_path)
            
            current_path.pop()

        dfs(root, [])
        return paths

