class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        first_zero = binary.find('0')
        if first_zero == -1:
            return binary
        zero_count = binary.count('0')
        prefix = '1' * first_zero
        middle_ones = '1' * (zero_count - 1)
        suffix = '1' * (n - first_zero - zero_count)
        return prefix + middle_ones + '0' + suffix
