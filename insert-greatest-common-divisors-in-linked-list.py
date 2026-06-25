from math import gcd
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        while curr.next:
            g = gcd(curr.val, curr.next.val)
            new_node = ListNode(g)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        return head
