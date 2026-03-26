import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 1
        q = collections.deque([(root, 0)])

        while q:
            level_size = len(q)
            
            first_idx_on_level = q[0][1]
            last_idx_on_level = q[-1][1]
            
            current_level_width = last_idx_on_level - first_idx_on_level + 1
            max_width = max(max_width, current_level_width)

            for _ in range(level_size):
                node, index = q.popleft()
                
                relative_idx_of_parent = index - first_idx_on_level
                
                if node.left:
                    q.append((node.left, 2 * relative_idx_of_parent))
                if node.right:
                    q.append((node.right, 2 * relative_idx_of_parent + 1))
                    
        return max_width