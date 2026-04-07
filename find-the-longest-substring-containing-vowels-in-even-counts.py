class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        max_len = 0
        current_mask = 0
        
        seen_masks = {0: -1} 
        
        for i, char in enumerate(s):
            if char in vowel_map:
                current_mask ^= (1 << vowel_map[char])
            
            if current_mask in seen_masks:
                max_len = max(max_len, i - seen_masks[current_mask])
            else:
                seen_masks[current_mask] = i
                
        return max_len
