import math
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1000000007
        maxv = 200
        dp = [[0]*(maxv+1) for _ in range(maxv+1)]
        dp[0][0] = 1
        for x in nums:
            ndp = [row[:] for row in dp]
            for g1 in range(maxv+1):
                for g2 in range(maxv+1):
                    val = dp[g1][g2]
                    if not val:
                        continue
                    ng1 = math.gcd(g1, x) if g1 else x
                    ndp[ng1][g2] = (ndp[ng1][g2] + val) % MOD
                    ng2 = math.gcd(g2, x) if g2 else x
                    ndp[g1][ng2] = (ndp[g1][ng2] + val) % MOD
            dp = ndp
        ans = 0
        for g in range(1, maxv+1):
            ans = (ans + dp[g][g]) % MOD
        return ans