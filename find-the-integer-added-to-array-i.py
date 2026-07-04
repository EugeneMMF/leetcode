from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sorted(nums1)
        s2 = sorted(nums2)
        return s2[0] - s1[0]
