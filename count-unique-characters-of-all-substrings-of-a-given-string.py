class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        
        char_indices = [[] for _ in range(26)] 
        
        for i in range(n):
            char_indices[ord(s[i]) - ord('A')].append(i)
        
        total_sum = 0
        
        for indices in char_indices:
            indices = [-1] + indices + [n]
            
            for k in range(1, len(indices) - 1):
                left_options = indices[k] - indices[k-1]
                right_options = indices[k+1] - indices[k]
                
                total_sum += left_options * right_options
                
        return total_sum
