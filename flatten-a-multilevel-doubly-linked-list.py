
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        current = head
        
        while current:
            if current.child:
                next_node_after_child = current.next
                
                current.next = current.child
                current.child.prev = current
                
                temp = current.child
                while temp.next:
                    temp = temp.next
                
                temp.next = next_node_after_child
                if next_node_after_child:
                    next_node_after_child.prev = temp
                
                current.child = None
            
            current = current.next
            
        return head
