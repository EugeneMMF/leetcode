class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (k + maxPts)
        
        dp[0] = 1.0
        
        current_window_sum = 1.0 
        
        ans = 0.0
        
        for i in range(1, k + maxPts):
            dp[i] = current_window_sum / maxPts
            
            if i >= k:
                if i <= n:
                    ans += dp[i]
            else: 
                current_window_sum += dp[i]
            
            if i - maxPts >= 0:
                if i - maxPts < k: 
                    current_window_sum -= dp[i - maxPts]
                    
        return ans
