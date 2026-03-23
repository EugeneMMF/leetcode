
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            if quadTree1.val:
                return Node(True, True)
            else:
                return quadTree2

        if quadTree2.isLeaf:
            if quadTree2.val:
                return Node(True, True)
            else:
                return quadTree1

        topLeft_res = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight_res = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft_res = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight_res = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if (topLeft_res.isLeaf and topRight_res.isLeaf and 
            bottomLeft_res.isLeaf and bottomRight_res.isLeaf and 
            topLeft_res.val == topRight_res.val == bottomLeft_res.val == bottomRight_res.val):
            
            return Node(topLeft_res.val, True)
        
        return Node(False, False, topLeft_res, topRight_res, bottomLeft_res, bottomRight_res)

