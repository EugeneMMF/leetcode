from typing import List
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for num, cnt in freq.items():
            if cnt == 1 and freq.get(num - 1, 0) == 0 and freq.get(num + 1, 0) == 0:
                res.append(num)
        return res
