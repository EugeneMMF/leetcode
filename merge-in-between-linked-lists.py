# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        prev = None
        cur = list1
        i = 0
        while i < a:
            prev = cur
            cur = cur.next
            i += 1
        pre = prev
        while i <= b:
            cur = cur.next
            i += 1
        post = cur
        pre.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = post
        return list1
