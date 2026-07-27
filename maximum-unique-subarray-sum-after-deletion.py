class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positives = {x for x in nums if x > 0}
        if positives:
            return sum(positives)
        return max(nums)
