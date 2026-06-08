# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        max_val = -1
        new_head = None
        while stack:
            node = stack.pop()
            if node.val >= max_val:
                max_val = node.val
                node.next = new_head
                new_head = node
        return new_head
