class Solution:
    def searchBST(self, root: 'Optional[TreeNode]', val: int) -> 'Optional[TreeNode]':
        current = root
        while current:
            if current.val == val:
                return current
            elif current.val < val:
                current = current.right
            else:
                current = current.left
        return None

