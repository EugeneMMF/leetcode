from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()
        for a,b,c in permutations(digits,3):
            if a==0: continue
            if c%2: continue
            nums.add(a*100 + b*10 + c)
        return sorted(nums)
