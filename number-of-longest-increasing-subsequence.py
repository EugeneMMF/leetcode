
class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [[1, 1] for _ in range(n)]
        
        max_len = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    current_len_at_j = dp[j][0]
                    current_count_at_j = dp[j][1]
                    
                    if current_len_at_j + 1 > dp[i][0]:
                        dp[i][0] = current_len_at_j + 1
                        dp[i][1] = current_count_at_j
                    elif current_len_at_j + 1 == dp[i][0]:
                        dp[i][1] += current_count_at_j
            
            max_len = max(max_len, dp[i][0])
            
        result_count = 0
        for i in range(n):
            if dp[i][0] == max_len:
                result_count += dp[i][1]
                
        return result_count
