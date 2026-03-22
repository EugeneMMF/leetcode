class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        sum_map = {0: -1}
        max_length = 0
        current_sum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                current_sum -= 1
            else:
                current_sum += 1

            if current_sum in sum_map:
                max_length = max(max_length, i - sum_map[current_sum])
            else:
                sum_map[current_sum] = i
        
        return max_length
