class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode

        from collections import deque
        q = deque()
        q.append(root)
        
        current_depth = 1

        while q:
            if current_depth == depth - 1:
                level_size = len(q)
                for _ in range(level_size):
                    cur_node = q.popleft()
                    
                    original_left = cur_node.left
                    original_right = cur_node.right

                    new_left_node = TreeNode(val)
                    new_right_node = TreeNode(val)

                    new_left_node.left = original_left
                    new_right_node.right = original_right

                    cur_node.left = new_left_node
                    cur_node.right = new_right_node
                return root

            level_size = len(q)
            for _ in range(level_size):
                cur_node = q.popleft()
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            
            current_depth += 1
        
        return root