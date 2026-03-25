# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        h = height(root)
        m = h + 1
        n = 2**(h + 1) - 1
        res = [["" for _ in range(n)] for _ in range(m)]

        def fill(node, r, c):
            if not node:
                return
            res[r][c] = str(node.val)
            fill(node.left, r + 1, c - (2**(h - r - 1)))
            fill(node.right, r + 1, c + (2**(h - r - 1)))

        fill(root, 0, (n - 1) // 2)
        return res

