class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        sorted_indices = sorted(range(len(nums)), key=lambda i: nums[i])
        i = j = 0
        count = 0
        n = len(nums)
        while i < n and j < n:
            if sorted_nums[j] > nums[sorted_indices[i]]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count