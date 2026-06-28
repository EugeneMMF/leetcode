class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 1000000007
        total = sum(nums)
        dp = [0] * (total + 1)
        dp[0] = 1
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        zero_count = freq.pop(0, 0)
        for v, c in freq.items():
            new_dp = [0] * (total + 1)
            for r0 in range(v):
                sum_window = 0
                window = []
                idx = r0
                while idx <= total:
                    sum_window = (sum_window + dp[idx]) % MOD
                    if len(window) > c:
                        sum_window = (sum_window - window.pop(0)) % MOD
                    new_dp[idx] = sum_window
                    window.append(dp[idx])
                    idx += v
            dp = new_dp
        if zero_count:
            factor = zero_count + 1
            for i in range(total + 1):
                dp[i] = dp[i] * factor % MOD
        ans = 0
        for s in range(l, r + 1):
            if s <= total:
                ans = (ans + dp[s]) % MOD
        return ans
