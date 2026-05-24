class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        best = nums[0]
        for num in nums:
            if abs(num) < abs(best) or (abs(num) == abs(best) and num > best):
                best = num
        return best
