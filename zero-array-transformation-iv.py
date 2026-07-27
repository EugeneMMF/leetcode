class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        max_sum = max(nums)
        masks = [1] * n
        if all(num == 0 for num in nums):
            return 0
        for k, (l, r, val) in enumerate(queries, 1):
            shift = val
            for i in range(l, r + 1):
                masks[i] |= masks[i] << shift
                masks[i] &= (1 << (max_sum + 1)) - 1
            if all((masks[i] >> nums[i]) & 1 for i in range(n)):
                return k
        return -1