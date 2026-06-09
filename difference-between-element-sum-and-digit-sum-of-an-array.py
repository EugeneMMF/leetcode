from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            while num:
                digit_sum += num % 10
                num //= 10
        return abs(element_sum - digit_sum)
