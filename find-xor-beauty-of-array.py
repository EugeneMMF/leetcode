class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        res = 0
        for v in nums:
            res ^= v
        return res
