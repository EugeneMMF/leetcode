class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2 * n - 2
        i = (time % cycle) + 1
        if i <= n:
            return i
        return 2 * n - i