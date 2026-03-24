class Solution:
    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def fractionAddition(self, expression: str) -> str:
        total_num = 0
        total_den = 1
        
        i = 0
        n = len(expression)
        
        while i < n:
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            
            start_num = i
            while i < n and expression[i].isdigit():
                i += 1
            numerator = int(expression[start_num:i])
            
            i += 1
            
            start_den = i
            while i < n and expression[i].isdigit():
                i += 1
            denominator = int(expression[start_den:i])
            
            current_frac_num = sign * numerator
            current_frac_den = denominator
            
            total_num = total_num * current_frac_den + current_frac_num * total_den
            total_den = total_den * current_frac_den
            
        if total_num == 0:
            return "0/1"
            
        common_divisor = self._gcd(abs(total_num), abs(total_den))
        
        total_num //= common_divisor
        total_den //= common_divisor
        
        return str(total_num) + "/" + str(total_den)
