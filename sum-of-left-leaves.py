
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total_sum = 0

        def dfs(node, is_left_child):
            nonlocal total_sum
            if not node:
                return

            if not node.left and not node.right and is_left_child:
                total_sum += node.val
            
            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, False)
        return total_sum
