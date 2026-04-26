from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total = 0
        max_len = 0
        for x in nums:
            total += bin(x).count('1')
            l = x.bit_length()
            if l > max_len:
                max_len = l
        if max_len == 0:
            return 0
        return total + max_len - 1
