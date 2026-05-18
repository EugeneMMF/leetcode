# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        group_size = 1
        while current:
            tail = current
            count = 0
            while count < group_size and tail:
                tail = tail.next
                count += 1
            if count % 2 == 0:
                rev_head, rev_tail = None, None
                node = current
                for _ in range(count):
                    nxt = node.next
                    node.next = rev_head
                    rev_head = node
                    rev_tail = node if rev_tail is None else rev_tail
                    node = nxt
                prev.next = rev_head
                rev_tail.next = tail
                prev = rev_tail
                current = tail
            else:
                prev = current
                for _ in range(count - 1):
                    prev = prev.next
                current = tail
            group_size += 1
        return dummy.next