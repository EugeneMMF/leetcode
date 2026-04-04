class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        res_digits = []
        while n != 0:
            remainder = n % (-2)
            
            if remainder == -1:
                remainder = 1
                n = (n // -2) + 1
            else:
                n = n // -2
            
            res_digits.append(str(remainder))
        
        return "".join(res_digits[::-1])
