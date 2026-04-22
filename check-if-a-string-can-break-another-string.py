class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a = sorted(s1)
        b = sorted(s2)
        can1 = all(x >= y for x, y in zip(a, b))
        can2 = all(y >= x for x, y in zip(a, b))
        return can1 or can2
