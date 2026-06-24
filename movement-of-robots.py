class Solution:
    def sumDistance(self, nums, s, d):
        M = 10**9 + 7
        n = len(nums)
        pos = [nums[i] + (d if s[i] == 'R' else -d) for i in range(n)]
        pos.sort()
        res = 0
        for i, val in enumerate(pos):
            coeff = 2 * i - n + 1
            res = (res + val * coeff) % M
        return res
