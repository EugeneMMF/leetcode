class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        pop = [x.bit_count() for x in nums]
        for i in range(n):
            for j in range(i):
                if pop[i] != pop[j] and nums[j] > nums[i]:
                    return False
        return True
