
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.current_val = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []

        def _inorder_traverse(node, is_counting_max_frequency: bool):
            if not node:
                return

            _inorder_traverse(node.left, is_counting_max_frequency)

            if self.current_val is None or node.val != self.current_val:
                self.current_val = node.val
                self.current_count = 1
            else:
                self.current_count += 1

            if is_counting_max_frequency:
                if self.current_count > self.max_count:
                    self.max_count = self.current_count
            else:
                if self.current_count == self.max_count:
                    self.modes.append(node.val)

            _inorder_traverse(node.right, is_counting_max_frequency)

        _inorder_traverse(root, True)

        self.current_val = None
        self.current_count = 0

        _inorder_traverse(root, False)

        return self.modes
