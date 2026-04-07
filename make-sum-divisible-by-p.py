class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = sum(nums) % p

        if target == 0:
            return 0

        prefix_sum_mod = {0: -1}
        current_sum_mod = 0
        min_len = n

        for i, num in enumerate(nums):
            current_sum_mod = (current_sum_mod + num) % p
            remainder = (current_sum_mod - target + p) % p

            if remainder in prefix_sum_mod:
                min_len = min(min_len, i - prefix_sum_mod[remainder])

            prefix_sum_mod[current_sum_mod] = i

        return min_len if min_len < n else -1
