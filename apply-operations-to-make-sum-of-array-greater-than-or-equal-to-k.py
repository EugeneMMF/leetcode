class Solution:
    def minOperations(self, k: int) -> int:
        min_ops = 10**9
        for x in range(1, k + 1):
            t = (k + x - 1) // x - 1
            ops = (x - 1) + t
            if ops < min_ops:
                min_ops = ops
        return min_ops