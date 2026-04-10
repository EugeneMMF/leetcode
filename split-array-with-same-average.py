class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        
        possible_sums = [set() for _ in range(n // 2 + 1)]
        possible_sums[0].add(0)
        
        for num in nums:
            for i in range(n // 2, 0, -1):
                for prev_sum in possible_sums[i - 1]:
                    possible_sums[i].add(prev_sum + num)
                    
        for i in range(1, n // 2 + 1):
            for s in possible_sums[i]:
                if s * n == total_sum * i:
                    return True
        
        return False

