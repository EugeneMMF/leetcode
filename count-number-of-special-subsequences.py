class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp0 = dp1 = dp2 = 0
        for num in nums:
            if num == 0:
                dp0 = (dp0 * 2 + 1) % MOD
            elif num == 1:
                dp1 = (dp1 * 2 + dp0) % MOD
            else:
                dp2 = (dp2 * 2 + dp1) % MOD
        return dp2