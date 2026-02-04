from typing import List, Optional
import bisect

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    orderedList = []
    while head:
      bisect.insort(orderedList, head, key=lambda x: x.val)
      head = head.next
    for i in range(len(orderedList)-1):
      orderedList[i].next = orderedList[i+1]
    orderedList[-1].next = None
    return orderedList[0]