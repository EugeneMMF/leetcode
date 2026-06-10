from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            for ch in str(num):
                res.append(int(ch))
        return res