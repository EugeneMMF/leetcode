class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 0
        for i in range(1, n + 1):
            bits = i.bit_length()
            ans = ((ans << bits) + i) % mod
        return ans
