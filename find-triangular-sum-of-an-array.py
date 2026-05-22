class Solution:
    def triangularSum(self, nums):
        n = len(nums)
        comb = 1
        res = 0
        for i in range(n):
            res = (res + comb * nums[i]) % 10
            if i < n - 1:
                comb = comb * (n - 1 - i) // (i + 1)
        return res
