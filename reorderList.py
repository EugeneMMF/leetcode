from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    nodes = []
    while head:
      nodes.append(head)
      head = head.next
    l = len(nodes)
    ll = l-1
    for i in range(round(l/2)):
      nodes[i].next = nodes[ll-i]
      nodes[ll-i].next = nodes[i+1]
    nodes[l//2].next = None