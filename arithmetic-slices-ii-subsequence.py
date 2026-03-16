
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        total_count = 0
        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                count_j = dp[j].get(diff, 0)
                
                total_count += count_j
                
                dp[i][diff] = dp[i].get(diff, 0) + count_j + 1
        
        return total_count
