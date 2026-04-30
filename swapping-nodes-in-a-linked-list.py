class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        for _ in range(k - 1):
            first = first.next
        kth_start = first
        second = head
        fast = first
        while fast.next:
            fast = fast.next
            second = second.next
        kth_end = second
        kth_start.val, kth_end.val = kth_end.val, kth_start.val
        return head
