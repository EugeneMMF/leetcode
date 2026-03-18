class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_result = x ^ y
        return bin(xor_result).count('1')
