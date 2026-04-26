class Solution:
    def minOperations(self, n: int) -> int:
        start = (n + 1) // 2
        return start * (n - start)
