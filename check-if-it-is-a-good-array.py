from typing import List
from math import gcd

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = 0
        for x in nums:
            g = gcd(g, x)
            if g == 1:
                return True
        return g == 1
