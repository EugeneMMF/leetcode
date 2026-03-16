from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        p_freq = [0] * 26
        s_window_freq = [0] * 26
        
        for char_p in p:
            p_freq[ord(char_p) - ord('a')] += 1

        result = []
        
        for i in range(m):
            s_window_freq[ord(s[i]) - ord('a')] += 1
        
        if s_window_freq == p_freq:
            result.append(0)
        
        for i in range(1, n - m + 1):
            left_char_idx = ord(s[i-1]) - ord('a')
            s_window_freq[left_char_idx] -= 1

            right_char_idx = ord(s[i + m - 1]) - ord('a')
            s_window_freq[right_char_idx] += 1
            
            if s_window_freq == p_freq:
                result.append(i)
                
        return result
