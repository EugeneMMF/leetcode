
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_counts = {}

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            current_sum = node.val + left_sum + right_sum
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1
            
            return current_sum

        dfs(root)

        if not sum_counts:
            return []

        max_freq = 0
        for count in sum_counts.values():
            if count > max_freq:
                max_freq = count
        
        result = []
        for s, count in sum_counts.items():
            if count == max_freq:
                result.append(s)

        return result
