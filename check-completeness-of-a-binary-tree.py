from collections import deque

class Solution:
    def isCompleteTree(self, root):
        q = deque([root])
        end = False
        while q:
            node = q.popleft()
            if not node:
                end = True
                continue
            if end:
                return False
            q.append(node.left)
            q.append(node.right)
        return True
