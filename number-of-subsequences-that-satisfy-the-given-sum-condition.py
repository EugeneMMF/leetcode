from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        i, j = 0, n - 1
        ans = 0
        while i <= j:
            if nums[i] + nums[j] <= target:
                ans = (ans + pow2[j - i]) % MOD
                i += 1
            else:
                j -= 1
        return ans
