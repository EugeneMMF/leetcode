class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k & ~n:
            return -1
        return bin(n & ~k).count('1')