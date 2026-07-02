import collections
from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        for count in freq.values():
            if count > 2:
                return False
        return True
