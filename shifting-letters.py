class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        n = len(s)
        result_chars = list(s)
        
        current_total_shift = 0
        
        for i in range(n - 1, -1, -1):
            current_total_shift = (current_total_shift + shifts[i]) % 26
            
            original_pos = ord(s[i]) - ord('a')
            
            new_pos = (original_pos + current_total_shift) % 26
            
            result_chars[i] = chr(ord('a') + new_pos)
            
        return "".join(result_chars)
