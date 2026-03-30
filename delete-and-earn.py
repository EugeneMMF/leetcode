class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_val = 0
        for num in nums:
            if num > max_val:
                max_val = num
        
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
        
        dp = [0] * (max_val + 1)
        
        dp[0] = 0 
        dp[1] = points[1]
        
        for i in range(2, max_val + 1):
            dp[i] = max(dp[i-1], points[i] + dp[i-2])
            
        return dp[max_val]
