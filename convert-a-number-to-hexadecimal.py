class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num += (1 << 32)

        hex_digits = []
        hex_map = "0123456789abcdef"

        while num > 0:
            remainder = num % 16
            hex_digits.append(hex_map[remainder])
            num //= 16
        
        return "".join(hex_digits[::-1])
