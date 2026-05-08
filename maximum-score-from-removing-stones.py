class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        total = a + b + c
        return min(total - max(a, b, c), total // 2)
