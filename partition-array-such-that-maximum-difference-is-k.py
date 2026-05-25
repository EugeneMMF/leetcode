class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i = 0
        n = len(nums)
        while i < n:
            count += 1
            start = nums[i]
            while i < n and nums[i] - start <= k:
                i += 1
        return count