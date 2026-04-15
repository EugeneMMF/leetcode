from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes=[]
        q=deque([(root,0,0)])
        while q:
            node,row,col=q.popleft()
            nodes.append((col,row,node.val))
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        nodes.sort()
        res=[]
        curcol=None
        for col,row,val in nodes:
            if col!=curcol:
                res.append([])
                curcol=col
            res[-1].append(val)
        return res
