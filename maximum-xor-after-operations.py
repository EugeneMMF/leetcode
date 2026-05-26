class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        or_val = 0
        for num in nums:
            or_val |= num
        return or_val
