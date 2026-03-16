class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []
        for i in range(len(nums)):
            num = abs(nums[i])
            index_to_check = num - 1
            if nums[index_to_check] < 0:
                duplicates.append(num)
            else:
                nums[index_to_check] = -nums[index_to_check]
        return duplicates
