# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        node = head.next
        total = 0
        while node:
            if node.val == 0:
                cur.next = ListNode(total)
                cur = cur.next
                total = 0
            else:
                total += node.val
            node = node.next
        return dummy.next
