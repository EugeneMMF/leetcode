class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        
        current_sum = 0
        
        if low <= root.val <= high:
            current_sum += root.val
        
        if root.val > low:
            current_sum += self.rangeSumBST(root.left, low, high)
            
        if root.val < high:
            current_sum += self.rangeSumBST(root.right, low, high)
            
        return current_sum
