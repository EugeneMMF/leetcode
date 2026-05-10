from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        mask = (1 << maximumBit) - 1
        prefix = [0]*n
        xor = 0
        for i, val in enumerate(nums):
            xor ^= val
            prefix[i] = xor
        ans = [0]*n
        for j in range(n):
            current = prefix[n-j-1]
            ans[j] = mask ^ current
        return ans
