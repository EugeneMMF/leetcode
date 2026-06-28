class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        z1 = nums1.count(0)
        z2 = nums2.count(0)
        if z1 and z2:
            return max(sum1 + z1, sum2 + z2)
        if z1:
            min1 = sum1 + z1
            return sum2 if sum2 >= min1 else -1
        if z2:
            min2 = sum2 + z2
            return sum1 if sum1 >= min2 else -1
        return sum1 if sum1 == sum2 else -1
