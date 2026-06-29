class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                x = nums[i]
                y = nums[j]
                if abs(x - y) <= min(x, y):
                    val = x ^ y
                    if val > max_xor:
                        max_xor = val
        return max_xor
