# Definition for a binary tree node.
# class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        dummy_head = TreeNode(0)
        self.prev = dummy_head
        
        def inorder_traverse(node):
            if not node:
                return
            
            inorder_traverse(node.left)
            
            node.left = None
            self.prev.right = node
            self.prev = node
            
            inorder_traverse(node.right)
            
        inorder_traverse(root)
        
        return dummy_head.right
