class Solution:
    def waysToSplit(self, nums):
        n = len(nums)
        pref = [0] * (n + 1)
        for i, v in enumerate(nums):
            pref[i + 1] = pref[i] + v
        total = pref[n]
        mod = 10**9 + 7
        ans = 0
        l = r = 0
        for i in range(n - 2):
            left = pref[i + 1]
            if l < i + 1:
                l = i + 1
            while l < n - 1 and pref[l + 1] - left < left:
                l += 1
            if r < l - 1:
                r = l - 1
            while r + 1 < n - 1 and 2 * pref[r + 2] <= total + left:
                r += 1
            if l <= r:
                ans += r - l + 1
        return ans % mod
