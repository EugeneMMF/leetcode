from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def ok(x):
            while x:
                if x % 10 == 0:
                    return False
                x //= 10
            return True
        for a in range(1, n):
            b = n - a
            if ok(a) and ok(b):
                return [a, b]
