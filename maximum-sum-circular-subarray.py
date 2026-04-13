class Solution:
    def maxSubarraySumCircular(self, nums):
        max_ending = max_sofar = nums[0]
        min_ending = min_sofar = nums[0]
        total = nums[0]
        for x in nums[1:]:
            max_ending = x if max_ending < 0 else max_ending + x
            max_sofar = max(max_sofar, max_ending)
            min_ending = x if min_ending > 0 else min_ending + x
            min_sofar = min(min_sofar, min_ending)
            total += x
        if max_sofar < 0:
            return max_sofar
        return max(max_sofar, total - min_sofar)
