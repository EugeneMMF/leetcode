class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        total = sum(nums)
        dp = [0] * k
        dp[0] = 1
        for val in nums:
            newdp = dp[:]
            if val < k:
                for s in range(val, k):
                    newdp[s] = (newdp[s] + dp[s - val]) % MOD
            dp = newdp
        count_less = sum(dp) % MOD
        count_both_less = 0
        if total < 2 * k:
            start = max(0, total - k + 1)
            count_both_less = sum(dp[start:k]) % MOD
        total_assign = pow(2, n, MOD)
        res = (total_assign - count_less - count_less + count_both_less) % MOD
        return res