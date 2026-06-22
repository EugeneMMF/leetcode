class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        nums.sort()
        pow2 = [1]*(n)
        inv2 = pow(2, mod-2, mod)
        inv2pow = [1]*(n)
        for i in range(1, n):
            pow2[i] = pow2[i-1]*2 % mod
            inv2pow[i] = inv2pow[i-1]*inv2 % mod
        W = [0]*n
        W[0] = nums[0]*inv2pow[0] % mod
        for i in range(1, n):
            W[i] = (W[i-1] + nums[i]*inv2pow[i]) % mod
        ans = 0
        for j in range(1, n):
            term = nums[j]*nums[j] % mod
            contrib = term * pow2[j-1] % mod
            contrib = contrib * W[j-1] % mod
            ans = (ans + contrib) % mod
        for x in nums:
            ans = (ans + x*x%mod*x)%mod
        return ans % mod