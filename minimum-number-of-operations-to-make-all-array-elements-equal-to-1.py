import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = [i for i, v in enumerate(nums) if v == 1]
        if ones:
            return n - len(ones)
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        if min_len == float('inf'):
            return -1
        return (min_len - 1) + (n - 1)
