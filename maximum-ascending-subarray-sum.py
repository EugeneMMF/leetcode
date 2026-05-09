class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        prev = -1
        for num in nums:
            if num > prev:
                current_sum += num
            else:
                current_sum = num
            if current_sum > max_sum:
                max_sum = current_sum
            prev = num
        return max_sum
