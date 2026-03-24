class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        current_max = nums[0]
        end = -1

        for i in range(1, n):
            if nums[i] < current_max:
                end = i
            else:
                current_max = nums[i]
        
        if end == -1:
            return 0

        current_min = nums[n - 1]
        start = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > current_min:
                start = i
            else:
                current_min = nums[i]
        
        return end - start + 1
