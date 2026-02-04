from typing import List, Optional
import bisect

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: return head
    orderedList = []
    while head:
      orderedList.append(head)
      head = head.next
    orderedList.sort(key=lambda x:x.val)
    for i in range(len(orderedList)-1):
      orderedList[i].next = orderedList[i+1]
    orderedList[-1].next = None
    return orderedList[0]