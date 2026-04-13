from collections import deque
from typing import Optional

class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque()
        bfs = deque([root]) if root else deque()
        while bfs:
            node = bfs.popleft()
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
            if not (node.left and node.right):
                self.q.append(node)
    def insert(self, val: int) -> int:
        parent = self.q[0]
        new_node = TreeNode(val)
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.q.popleft()
        self.q.append(new_node)
        return parent.val
    def get_root(self) -> Optional[TreeNode]:
        return self.root
