# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        to_delete_set = set(to_delete)
        result = []

        def dfs(node, is_parent_deleted):
            if not node:
                return None

            current_node_deleted = node.val in to_delete_set

            node.left = dfs(node.left, current_node_deleted)
            node.right = dfs(node.right, current_node_deleted)

            if not current_node_deleted and is_parent_deleted:
                result.append(node)
            
            if current_node_deleted:
                return None
            else:
                return node

        dfs(root, True)
        
        return result
