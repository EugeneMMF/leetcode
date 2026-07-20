class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        period = 2 * (n - 1)
        pos = k % period
        if pos < n:
            return pos
        return period - pos