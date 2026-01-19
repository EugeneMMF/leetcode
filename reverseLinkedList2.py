from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
      return head
    pos = 1
    prev = head
    current = head
    nxt = current.next
    reversal = []
    start = None
    end = None
    if left == 1:
      reversal.append(current)
    while nxt:
      current = nxt
      nxt = current.next
      pos += 1
      if pos >= left and pos <= right:
        reversal.append(current)
      if pos == right:
        end = nxt
      if pos == left:
        start = prev
      prev = current
    for i in range(len(reversal)-1, 0, -1):
      reversal[i].next = reversal[i-1]
    reversal[0].next = end
    if start:
      start.next = reversal[-1]
      return head
    return reversal[-1]