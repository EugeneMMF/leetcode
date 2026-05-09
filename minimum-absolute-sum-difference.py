class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        from bisect import bisect_left
        MOD = 10**9 + 7
        sorted_nums1 = sorted(nums1)
        total = 0
        max_reduction = 0
        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            total = (total + diff) % MOD
            idx = bisect_left(sorted_nums1, b)
            best_new = diff
            if idx < len(sorted_nums1):
                best_new = min(best_new, abs(sorted_nums1[idx] - b))
            if idx > 0:
                best_new = min(best_new, abs(sorted_nums1[idx - 1] - b))
            max_reduction = max(max_reduction, diff - best_new)
        return (total - max_reduction) % MOD