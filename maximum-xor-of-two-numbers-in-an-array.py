class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        if not nums:
            return 0

        L = 30 

        root = TrieNode()

        for num in nums:
            node = root
            for i in range(L, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        max_xor_result = 0

        for num in nums:
            node = root
            current_xor = 0
            for i in range(L, -1, -1):
                bit = (num >> i) & 1
                
                desired_bit = 1 - bit
                
                if node.children[desired_bit]:
                    current_xor |= (1 << i)
                    node = node.children[desired_bit]
                else:
                    node = node.children[bit]
            
            max_xor_result = max(max_xor_result, current_xor)
            
        return max_xor_result
