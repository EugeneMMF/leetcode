class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ones = [i for i, x in enumerate(nums) if x == 1]
        if not ones:
            return 0
        if len(ones) == 1:
            return 1
        res = 1
        for i in range(1, len(ones)):
            res = res * (ones[i] - ones[i-1]) % MOD
        return res
