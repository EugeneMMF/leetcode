from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    headANodes = []
    headBNodes = []
    while headA:
      headANodes.append(headA)
      headA = headA.next
    while headB:
      headBNodes.append(headB)
      headB = headB.next
    intersection = None
    l = min(len(headANodes), len(headBNodes))
    for _ in range(l):
      node = headBNodes.pop()
      if id(node) != id(headANodes.pop()): break
      intersection = node
    return intersection