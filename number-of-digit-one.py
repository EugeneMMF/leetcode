class Solution:
    def countDigitOne(self, n: int) -> int:
        
        total_ones = 0
        pow10 = 1 

        while n // pow10 > 0 or pow10 == 1:
            
            higher = n // (pow10 * 10)
            
            current_digit = (n // pow10) % 10
            
            lower = n % pow10

            if current_digit == 0:
                total_ones += higher * pow10
            elif current_digit == 1:
                total_ones += higher * pow10 + lower + 1
            else:
                total_ones += (higher + 1) * pow10
            
            pow10 *= 10
        
        return total_ones
