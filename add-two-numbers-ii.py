# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        current = l1
        while current:
            stack1.append(current.val)
            current = current.next

        current = l2
        while current:
            stack2.append(current.val)
            current = current.next

        result_head = None
        carry = 0

        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            current_sum = val1 + val2 + carry
            new_digit = current_sum % 10
            carry = current_sum // 10

            new_node = ListNode(new_digit)
            new_node.next = result_head
            result_head = new_node

        return result_head