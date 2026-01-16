from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    nodes = []
    current = head
    while current is not None:
      nodes.append(current)
      current = current.next
    if k == 0:
      return head
    if len(nodes) == 1:
      return head
    if len(nodes) == 0:
      return
    k = k%len(nodes)
    nodes[-1].next = nodes[0]
    nodes[-k-1].next = None
    return nodes[-k]