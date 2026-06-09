class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        total_pos = 0
        sum_diff = 0
        for a, b in zip(nums1, nums2):
            diff = b - a
            sum_diff += diff
            if diff % k != 0:
                return -1
            if diff > 0:
                total_pos += diff
        if sum_diff != 0:
            return -1
        return total_pos // k
