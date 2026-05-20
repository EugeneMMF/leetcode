class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        sign = -1 if num < 0 else 1
        digits = list(str(abs(num)))
        if sign == 1:
            digits.sort()
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int(''.join(digits))
        else:
            digits.sort(reverse=True)
            return -int(''.join(digits))
