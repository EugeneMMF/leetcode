from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head
    current = head
    previous = head.val
    result = [head]
    while current.next:
      current = current.next
      if current.val != previous:
        result[-1].next = current
        result.append(current)
        previous = current.val
    if len(result):
      result[-1].next = None
      return result[0]
    return