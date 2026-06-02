# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        from collections import deque
        parent = {}
        start_node = None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == start:
                start_node = node
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        queue = deque([(start_node, 0)])
        visited = {start_node}
        max_time = 0
        while queue:
            node, t = queue.popleft()
            max_time = max(max_time, t)
            for nei in (node.left, node.right, parent.get(node)):
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, t + 1))
        return max_time
