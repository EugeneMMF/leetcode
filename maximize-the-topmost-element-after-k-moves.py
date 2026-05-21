class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            return -1 if k % 2 == 1 else nums[0]
        if k == 1:
            return nums[1]
        max_val = max(nums[:min(k - 1, n)])
        if k < n:
            max_val = max(max_val, nums[k])
        return max_val
