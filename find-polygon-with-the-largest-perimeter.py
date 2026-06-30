class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        for i in range(n-1, 1, -1):
            if nums[i] < prefix[i-1]:
                return prefix[i]
        return -1