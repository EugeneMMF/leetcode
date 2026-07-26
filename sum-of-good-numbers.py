class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            good = True
            if i - k >= 0:
                good &= nums[i] > nums[i - k]
            if i + k < n:
                good &= nums[i] > nums[i + k]
            if good:
                total += nums[i]
        return total
