class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False
        from collections import Counter
        cnt = Counter(nums)
        for i in range(1, n):
            if cnt.get(i, 0) != 1:
                return False
        if cnt.get(n, 0) != 2:
            return False
        return True
