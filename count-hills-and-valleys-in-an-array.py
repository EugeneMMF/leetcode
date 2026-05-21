from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        compressed = [nums[0]]
        for num in nums[1:]:
            if num != compressed[-1]:
                compressed.append(num)
        count = 0
        for i in range(1, len(compressed)-1):
            if compressed[i] > compressed[i-1] and compressed[i] > compressed[i+1]:
                count += 1
            elif compressed[i] < compressed[i-1] and compressed[i] < compressed[i+1]:
                count += 1
        return count
