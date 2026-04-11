# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s=set(nums)
        cnt=0
        cur=head
        while cur:
            if cur.val in s and (cur.next is None or cur.next.val not in s):
                cnt+=1
            cur=cur.next
        return cnt
