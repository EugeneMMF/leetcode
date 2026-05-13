class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        count = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                count += 1
                if count > 1:
                    return False
                if i > 1 and nums[i] <= nums[i - 2] and i < n - 1 and nums[i + 1] <= nums[i - 1]:
                    return False
        return True
