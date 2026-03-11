from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self._longestSubstring_recursive(s, 0, len(s), k)

    def _longestSubstring_recursive(self, s: str, start: int, end: int, k: int) -> int:
        if end - start < k:
            return 0
        
        counts = Counter(s[start:end])

        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            
            if counts[char] > 0 and counts[char] < k:
                max_len = 0
                current_segment_start = start
                
                for i in range(start, end):
                    if s[i] == char:
                        max_len = max(max_len, self._longestSubstring_recursive(s, current_segment_start, i, k))
                        current_segment_start = i + 1
                
                max_len = max(max_len, self._longestSubstring_recursive(s, current_segment_start, end, k))
                
                return max_len
        
        return end - start
