from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head: return
    previous = None
    while head and head.val == val:
      head = head.next
    root = head
    while head:
      if head.val == val:
        previous.next = head.next
        head = previous
      previous = head
      head = head.next
    return root