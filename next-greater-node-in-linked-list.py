# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: 'ListNode') -> list[int]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        n = len(values)
        answer = [0] * n
        stack = []

        for i in range(n):
            current_value = values[i]
            while stack and values[stack[-1]] < current_value:
                popped_index = stack.pop()
                answer[popped_index] = current_value
            
            stack.append(i)
        
        return answer
