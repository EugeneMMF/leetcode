class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 0:
                n >>= 1
            else:
                if n & 3 == 1:
                    n -= 1
                else:
                    n += 1
                count += 1
                n >>= 1
        return count
