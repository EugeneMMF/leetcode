class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0] * 26
        
        current_max_len = 0
        
        for i in range(len(s)):
            char_code = ord(s[i])
            
            if i == 0:
                current_max_len = 1
            else:
                prev_char_code = ord(s[i-1])
                if (char_code - prev_char_code + 26) % 26 == 1:
                    current_max_len += 1
                else:
                    current_max_len = 1
            
            dp[char_code - ord('a')] = max(dp[char_code - ord('a')], current_max_len)
            
        return sum(dp)
