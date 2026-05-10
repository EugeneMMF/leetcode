import typing

class Solution:
    def maxDistance(self, nums1: typing.List[int], nums2: typing.List[int]) -> int:
        i = 0
        j = 0
        ans = 0
        n1 = len(nums1)
        n2 = len(nums2)
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                if j >= i:
                    ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        return ans
