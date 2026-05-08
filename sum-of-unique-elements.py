class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        return sum(x for x, c in cnt.items() if c == 1)
