class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        total_moves = 0
        expected_min = 0

        for num in nums:
            current_val_to_use = max(num, expected_min)
            total_moves += current_val_to_use - num
            expected_min = current_val_to_use + 1
            
        return total_moves
