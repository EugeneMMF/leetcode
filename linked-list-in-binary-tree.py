# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head, root):
        def match(node, lst):
            if not node:
                return False
            if node.val != lst.val:
                return False
            if not lst.next:
                return True
            return match(node.left, lst.next) or match(node.right, lst.next)
        if not root:
            return False
        if match(root, head):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
