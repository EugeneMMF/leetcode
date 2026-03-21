from collections import deque
from typing import List, Optional

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            current_level_size = len(queue)
            current_max_val = float('-inf')

            for _ in range(current_level_size):
                node = queue.popleft()
                current_max_val = max(current_max_val, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_max_val)
        
        return result
