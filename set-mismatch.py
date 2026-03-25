class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicate = -1
        missing = -1
        n = len(nums)

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                duplicate = abs(num)
            else:
                nums[idx] = -nums[idx]
        
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break 
        
        return [duplicate, missing]
