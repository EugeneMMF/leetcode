
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverseList(node):
            prev = None
            curr = node
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        second_half_head = reverseList(slow.next)
        
        first_half_curr = head
        second_half_curr = second_half_head
        
        is_palindrome = True
        while second_half_curr:
            if first_half_curr.val != second_half_curr.val:
                is_palindrome = False
                break
            first_half_curr = first_half_curr.next
            second_half_curr = second_half_curr.next
            
        slow.next = reverseList(second_half_head)

        return is_palindrome
