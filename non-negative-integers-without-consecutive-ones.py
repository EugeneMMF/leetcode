class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, 31):
            dp[i] = dp[i-1] + dp[i-2]
            
        s = bin(n)[2:]
        k = len(s)
        
        ans = 0
        last_bit = 0
        
        for i in range(k):
            current_bit = int(s[i])
            remaining_length = k - 1 - i
            
            if current_bit == 1:
                ans += dp[remaining_length]
                
                if last_bit == 1:
                    return ans
            
            last_bit = current_bit
        
        ans += 1
        
        return ans
