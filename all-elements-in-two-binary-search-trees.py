# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(node, out):
            if not node:
                return
            inorder(node.left, out)
            out.append(node.val)
            inorder(node.right, out)
        a=[]
        b=[]
        inorder(root1, a)
        inorder(root2, b)
        i=j=0
        res=[]
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i]); i+=1
            else:
                res.append(b[j]); j+=1
        if i < len(a):
            res.extend(a[i:])
        if j < len(b):
            res.extend(b[j:])
        return res
