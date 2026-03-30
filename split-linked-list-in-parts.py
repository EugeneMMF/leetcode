
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        base_len = count // k
        remainder = count % k
        
        result = []
        current_node_ptr = head
        
        for i in range(k):
            part_len = base_len + (1 if i < remainder else 0)
            
            result.append(current_node_ptr)
            
            tail_of_current_part = current_node_ptr
            for _ in range(part_len - 1):
                if tail_of_current_part:
                    tail_of_current_part = tail_of_current_part.next
                else:
                    break
            
            if tail_of_current_part:
                next_part_head = tail_of_current_part.next
                tail_of_current_part.next = None
                current_node_ptr = next_part_head
            else:
                current_node_ptr = None
                
        return result
