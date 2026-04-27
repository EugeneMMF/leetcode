class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def helper(x: int) -> int:
            if x == 0:
                return 0
            k = x.bit_length() - 1
            msb = 1 << k
            return ((1 << (k + 1)) - 1) - helper(x - msb)
        return helper(n)
