class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        min_val = min(nums)
        max_val = max(nums)
        min_idx = nums.index(min_val)
        max_idx = nums.index(max_val)
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx
        front = max_idx + 1
        back = n - min_idx
        both = min_idx + 1 + n - max_idx
        return min(front, back, both)