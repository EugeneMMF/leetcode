class Solution:
    def maximumLength(self, nums):
        count_even = 0
        count_odd = 0
        dp_even = 0
        dp_odd = 0
        for x in nums:
            if x % 2 == 0:
                count_even += 1
                dp_even = max(dp_even, dp_odd + 1)
            else:
                count_odd += 1
                dp_odd = max(dp_odd, dp_even + 1)
        return max(count_even, count_odd, dp_even, dp_odd)
