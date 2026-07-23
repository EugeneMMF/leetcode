from math import gcd
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        def array_gcd(arr):
            res = arr[0]
            for x in arr[1:]:
                res = gcd(res, x)
            return res
        def array_lcm(arr):
            res = arr[0]
            for x in arr[1:]:
                res = lcm(res, x)
            return res
        n = len(nums)
        full_gcd = array_gcd(nums)
        full_lcm = array_lcm(nums)
        max_score = full_gcd * full_lcm
        for i in range(n):
            sub = nums[:i] + nums[i+1:]
            if sub:
                g = array_gcd(sub)
                l = array_lcm(sub)
                score = g * l
                if score > max_score:
                    max_score = score
        return max_score
