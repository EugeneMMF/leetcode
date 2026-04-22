from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                d[i + j].append(val)
        res = []
        for k in range(max(d.keys()) + 1):
            if k in d:
                res.extend(reversed(d[k]))
        return res
