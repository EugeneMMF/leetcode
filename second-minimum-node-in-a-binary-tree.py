class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1

        min1 = root.val
        second_min = float('inf')

        def dfs(node):
            nonlocal second_min
            
            if not node:
                return

            if node.val == min1:
                dfs(node.left)
                dfs(node.right)
            elif node.val < second_min:
                second_min = node.val
                
        dfs(root)

        return second_min if second_min != float('inf') else -1
