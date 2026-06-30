class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        half = len(nums1) // 2
        distinct1 = min(len(set(nums1)), half)
        distinct2 = min(len(set(nums2)), half)
        total_distinct = len(set(nums1) | set(nums2))
        return min(total_distinct, distinct1 + distinct2)
