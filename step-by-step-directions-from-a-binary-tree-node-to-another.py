# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent = {}
        start_node = None
        dest_node = None
        stack = [(root, None)]
        while stack:
            node, par = stack.pop()
            parent[node] = par
            if node.val == startValue:
                start_node = node
            if node.val == destValue:
                dest_node = node
            if node.right:
                stack.append((node.right, node))
            if node.left:
                stack.append((node.left, node))
        def build_path(node):
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]
        start_path = build_path(start_node)
        dest_path = build_path(dest_node)
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1
        lca_index = i - 1
        up_moves = 'U' * (len(start_path) - lca_index - 1)
        down_moves = ''
        for node in dest_path[lca_index+1:]:
            if parent[node] and node == parent[node].left:
                down_moves += 'L'
            else:
                down_moves += 'R'
        return up_moves + down_moves