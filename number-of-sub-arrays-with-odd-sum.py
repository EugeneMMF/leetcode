class Solution:
    def numOfSubarrays(self, arr):
        MOD = 1000000007
        even = 1
        odd = 0
        pref = 0
        for v in arr:
            pref ^= v & 1
            if pref == 0:
                even += 1
            else:
                odd += 1
        return (even * odd) % MOD
