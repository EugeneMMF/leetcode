# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque([root])
        total = 0
        while q:
            level_size = len(q)
            vals = []
            for _ in range(level_size):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sorted_vals = sorted(vals)
            index_map = {v:i for i,v in enumerate(sorted_vals)}
            visited = [False]*len(vals)
            for i in range(len(vals)):
                if visited[i] or index_map[vals[i]]==i:
                    visited[i] = True
                    continue
                cycle_len = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = index_map[vals[j]]
                    cycle_len += 1
                total += cycle_len-1
        return total