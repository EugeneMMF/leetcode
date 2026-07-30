from typing import List

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        digits = [len(str(x)) for x in nums]
        pow10_mod = [pow(10, d, k) for d in range(max(digits) + 1)]
        full = (1 << n) - 1
        dp = [[None] * k for _ in range(1 << n)]
        dp[0][0] = ()
        for mask in range(1 << n):
            for r in range(k):
                seq = dp[mask][r]
                if seq is None:
                    continue
                for i in range(n):
                    if mask >> i & 1:
                        continue
                    newmask = mask | (1 << i)
                    newr = (r * pow10_mod[digits[i]] + nums[i]) % k
                    cand = seq + (nums[i],)
                    if dp[newmask][newr] is None or cand < dp[newmask][newr]:
                        dp[newmask][newr] = cand
        res = dp[full][0]
        return list(res) if res is not None else []
