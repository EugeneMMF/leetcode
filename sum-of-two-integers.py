class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        a_val = a & mask
        b_val = b & mask

        while b_val != 0:
            sum_no_carry = a_val ^ b_val
            carry = ((a_val & b_val) << 1) & mask
            
            a_val = sum_no_carry
            b_val = carry
        
        if (a_val & 0x80000000) != 0:
            return ~(a_val ^ mask)
        else:
            return a_val
