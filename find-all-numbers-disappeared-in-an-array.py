class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for num in nums:
            index_to_mark = abs(num) - 1
            if nums[index_to_mark] > 0:
                nums[index_to_mark] *= -1
        
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result
