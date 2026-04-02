from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(nums)

        nums.sort()

        powers_of_2 = [1] * N
        for i in range(1, N):
            powers_of_2[i] = (powers_of_2[i-1] * 2) % MOD
        
        max_contrib_sum = 0
        min_contrib_sum = 0

        for i in range(N):
            max_contrib_sum = (max_contrib_sum + nums[i] * powers_of_2[i]) % MOD
            min_contrib_sum = (min_contrib_sum + nums[i] * powers_of_2[N - 1 - i]) % MOD
        
        total_width_sum = (max_contrib_sum - min_contrib_sum + MOD) % MOD
        
        return total_width_sum
