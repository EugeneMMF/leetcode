class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i1 = nums.index(1)
        iN = nums.index(n)
        if i1 < iN:
            return i1 + (n - 1 - iN)
        return i1 + (n - 1 - iN) - 1