class Solution:
    def rangeSum(self, nums, n, left, right):
        MOD = 10**9 + 7
        sums = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                sums.append(s)
        sums.sort()
        pref = [0]
        for v in sums:
            pref.append((pref[-1] + v) % MOD)
        return (pref[right] - pref[left - 1]) % MOD
