class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        d2 = 1 

        if s[0] == '*':
            d1 = 9
        elif s[0] == '0':
            d1 = 0
        else:
            d1 = 1
        
        if n == 1:
            return d1

        for i in range(2, n + 1):
            d_curr = 0
            
            char_s_i_minus_1 = s[i-1]
            if char_s_i_minus_1 == '*':
                d_curr = (d_curr + d1 * 9) % MOD
            elif char_s_i_minus_1 != '0':
                d_curr = (d_curr + d1) % MOD
            
            char_s_i_minus_2 = s[i-2]
            ways_two_chars = 0

            if char_s_i_minus_2 == '1':
                if char_s_i_minus_1 == '*':
                    ways_two_chars = 9
                else:
                    ways_two_chars = 1
            elif char_s_i_minus_2 == '2':
                if char_s_i_minus_1 == '*':
                    ways_two_chars = 6
                elif '0' <= char_s_i_minus_1 <= '6':
                    ways_two_chars = 1
            elif char_s_i_minus_2 == '*':
                if char_s_i_minus_1 == '*':
                    ways_two_chars = 15
                elif '0' <= char_s_i_minus_1 <= '6':
                    ways_two_chars = 2
                elif '7' <= char_s_i_minus_1 <= '9':
                    ways_two_chars = 1

            d_curr = (d_curr + d2 * ways_two_chars) % MOD
            
            d2 = d1
            d1 = d_curr
        
        return d1
