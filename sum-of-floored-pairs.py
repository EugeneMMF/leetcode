class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        maxV = max(nums)
        freq = [0] * (maxV + 1)
        for v in nums:
            freq[v] += 1
        pref = [0] * (maxV + 2)
        for i in range(1, maxV + 2):
            pref[i] = pref[i - 1] + freq[i - 1]
        total = 0
        for d in range(1, maxV + 1):
            if freq[d] == 0:
                continue
            s = 0
            for m in range(d, maxV + 1, d):
                l = m
                r = min(m + d - 1, maxV)
                cnt = pref[r + 1] - pref[l]
                t = m // d
                s += cnt * t
            total = (total + freq[d] * s) % MOD
        return total