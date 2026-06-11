class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if common:
            return min(common)
        res = 10**9
        for a in nums1:
            for b in nums2:
                res = min(res, 10*a+b, 10*b+a)
        return res
