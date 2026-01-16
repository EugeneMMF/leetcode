from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    startLeft = None
    startRight = None
    lastLeft = None
    lastRight = None
    current = head
    if not head:
      return None
    if current.val < x:
      startLeft = current
      lastLeft = current
    else:
      startRight = current
      lastRight = current
    while current.next:
      current = current.next
      if current.val < x:
        if startLeft:
          lastLeft.next = current
          lastLeft = current
        else:
          startLeft = current
          lastLeft = current
      elif startRight:
        lastRight.next = current
        lastRight = current
      else:
        startRight = current
        lastRight = current
    if lastRight:
      lastRight.next = None
    if lastLeft:
      lastLeft.next = startRight
      return startLeft
    else:
      return startRight