from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        target = 0
        for num in nums:
            if num < target:
                moves += target - num
            else:
                target = num
            target += 1
        return moves
