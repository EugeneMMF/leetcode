class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        import math
        g = 0
        for v in numsDivide:
            g = math.gcd(g, v)
        candidates = [x for x in nums if g % x == 0]
        if not candidates:
            return -1
        x = min(candidates)
        deletions = sum(1 for v in nums if v < x)
        return deletions