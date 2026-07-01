class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        target = nums[0] + nums[1]
        count = 1
        i = 2
        while i + 1 < n and nums[i] + nums[i+1] == target:
            count += 1
            i += 2
        return count
