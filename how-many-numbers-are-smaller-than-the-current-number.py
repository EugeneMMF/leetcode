class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_val = 100
        
        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1
        
        prefix_sum = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sum[i] = prefix_sum[i-1] + counts[i-1]
        
        result = []
        for num in nums:
            result.append(prefix_sum[num])
        
        return result
