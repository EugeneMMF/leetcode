class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefix_sums = {0: 1}
        self.count = 0

        def dfs(node, current_path_sum):
            if not node:
                return

            current_path_sum += node.val

            if (current_path_sum - targetSum) in prefix_sums:
                self.count += prefix_sums[current_path_sum - targetSum]

            prefix_sums[current_path_sum] = prefix_sums.get(current_path_sum, 0) + 1

            dfs(node.left, current_path_sum)
            dfs(node.right, current_path_sum)

            prefix_sums[current_path_sum] -= 1

        dfs(root, 0)
        return self.count
