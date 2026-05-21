from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        last = None
        pairs = 0
        for num in nums:
            if last is None:
                last = num
            else:
                if last != num:
                    pairs += 1
                    last = None
                else:
                    # skip current num to keep last for future pairing
                    continue
        return len(nums) - 2 * pairs