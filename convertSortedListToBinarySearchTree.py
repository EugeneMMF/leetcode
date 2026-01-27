from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    nums = []

    while head:
      nums.append(head.val)
      head = head.next

    def helper(start,end):
      if start == end: return None
      pivot = (start+end)//2
      root = TreeNode(nums[pivot])
      root.left = helper(start, pivot)
      root.right = helper(pivot+1, end)
      return root

    l = len(nums)
    if l == 0: return None
    return helper(0, l)