class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        total1 = 0
        total2 = 0
        max_ending = 0
        max_so_far = float('-inf')
        min_ending = 0
        min_so_far = float('inf')
        for i in range(n):
            a = nums1[i]
            b = nums2[i]
            total1 += a
            total2 += b
            diff = b - a
            max_ending = max(diff, max_ending + diff)
            max_so_far = max(max_so_far, max_ending)
            min_ending = min(diff, min_ending + diff)
            min_so_far = min(min_so_far, min_ending)
        ans = max(total1 + max_so_far, total2 - min_so_far, total1, total2)
        return ans
