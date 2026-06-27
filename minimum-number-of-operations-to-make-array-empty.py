class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        ops = 0
        for v in cnt.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                ops += v // 3
            elif v % 3 == 1:
                ops += (v - 4) // 3 + 2
            else:  # v % 3 == 2
                ops += (v - 2) // 3 + 1
        return ops
