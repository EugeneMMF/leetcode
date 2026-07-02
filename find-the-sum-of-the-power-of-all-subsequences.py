class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        max_k = k
        dp = [[0]*(n+1) for _ in range(max_k+1)]
        dp[0][0] = 1
        for val in nums:
            for s in range(max_k, val-1, -1):
                for m in range(n-1, -1, -1):
                    if dp[s-val][m]:
                        dp[s][m+1] = (dp[s][m+1] + dp[s-val][m]) % MOD
        pow2 = [1]*(n+1)
        for i in range(1, n+1):
            pow2[i] = (pow2[i-1]*2)%MOD
        ans = 0
        for m in range(1, n+1):
            cnt = dp[max_k][m]
            if cnt:
                ans = (ans + cnt * pow2[n-m]) % MOD
        return ans
