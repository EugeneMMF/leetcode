# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        sum_to_node = {0: dummy}
        node = head
        while node:
            prefix += node.val
            sum_to_node[prefix] = node
            node = node.next
        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            node.next = sum_to_node[prefix].next
            node = node.next
        return dummy.next
