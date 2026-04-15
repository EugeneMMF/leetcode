class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        diff = [0] * (n + 1)
        cur = 0
        res = 0
        for i in range(n):
            cur ^= diff[i]
            if (nums[i] ^ cur) == 0:
                if i + k > n:
                    return -1
                res += 1
                cur ^= 1
                diff[i + k] ^= 1
        return res
