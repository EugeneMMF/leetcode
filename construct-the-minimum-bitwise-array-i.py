class Solution:
    def minBitwiseArray(self, nums):
        res = []
        for p in nums:
            found = -1
            for x in range(p):
                if x | (x + 1) == p:
                    found = x
                    break
            res.append(found)
        return res
