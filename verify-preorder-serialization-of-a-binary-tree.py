class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        
        diff = 1 
        
        for i, node in enumerate(nodes):
            diff -= 1
            
            if diff < 0:
                return False
            
            if node != '#':
                diff += 2
            
            if diff == 0 and i < len(nodes) - 1:
                return False
                
        return diff == 0
