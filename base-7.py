class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)

        base7_digits = []
        while num > 0:
            base7_digits.append(str(num % 7))
            num //= 7
        
        base7_str = "".join(base7_digits[::-1])
        
        if is_negative:
            return "-" + base7_str
        else:
            return base7_str
