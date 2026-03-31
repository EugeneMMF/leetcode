class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 1
        
        dp_prev2 = 1 
        dp_up_prev2 = 0 

        dp_prev1 = 1 
        dp_up_prev1 = 0 
        
        for i in range(2, n + 1):
            dp_up_curr = (dp_up_prev1 + dp_prev2) % MOD
            dp_curr = (dp_prev1 + dp_prev2 + 2 * dp_up_prev1) % MOD
            
            dp_prev2 = dp_prev1
            dp_up_prev2 = dp_up_prev1
            dp_prev1 = dp_curr
            dp_up_prev1 = dp_up_curr
            
        return dp_prev1
