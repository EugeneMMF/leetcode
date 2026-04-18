class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        a = b = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    a += 1
                else:
                    b += 1
        if (a + b) % 2:
            return -1
        return a // 2 + b // 2 + (2 if a % 2 else 0)
