class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0

        temp_n = n
        while temp_n > 0:
            digit = temp_n % 10
            product_of_digits *= digit
            sum_of_digits += digit
            temp_n //= 10
        
        return product_of_digits - sum_of_digits
