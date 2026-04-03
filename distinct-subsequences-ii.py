class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * 26 
        
        total_distinct = 0
        
        for char_code in map(ord, s):
            char_idx = char_code - ord('a')
            
            new_subsequences_ending_with_char = (total_distinct + 1) % MOD
            
            subtrahend = dp[char_idx]
            
            dp[char_idx] = new_subsequences_ending_with_char
            
            total_distinct = (total_distinct + new_subsequences_ending_with_char - subtrahend + MOD) % MOD
            
        return total_distinct
