class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if t == 1:
            return n
        m = n
        while True:
            prod = 1
            temp = m
            if temp == 0:
                prod = 0
            else:
                while temp > 0:
                    d = temp % 10
                    prod *= d
                    temp //= 10
            if prod % t == 0:
                return m
            m += 1