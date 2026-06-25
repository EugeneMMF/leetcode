# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        carry = 0
        for node in reversed(nodes):
            val = node.val * 2 + carry
            node.val = val % 10
            carry = val // 10
        if carry:
            new_head = ListNode(carry)
            new_head.next = head
            return new_head
        return head
