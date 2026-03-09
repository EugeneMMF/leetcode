
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import random

class Solution:

    def __init__(self, head: ListNode):
        self.nodes_values = []
        current = head
        while current:
            self.nodes_values.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        random_index = random.randrange(len(self.nodes_values))
        return self.nodes_values[random_index]
