class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1 = 0
        for v in nums1:
            x1 ^= v
        x2 = 0
        for v in nums2:
            x2 ^= v
        res = 0
        if len(nums2) & 1:
            res ^= x1
        if len(nums1) & 1:
            res ^= x2
        return res