from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds = [nums[i] for i in range(1, len(nums), 2)]
        odds.sort(reverse=True)
        evens = [nums[i] for i in range(0, len(nums), 2)]
        evens.sort()
        odd_idx = 0
        even_idx = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evens[even_idx]
                even_idx += 1
            else:
                nums[i] = odds[odd_idx]
                odd_idx += 1
        return nums
