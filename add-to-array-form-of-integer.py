from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = 0
        res = []
        while i >= 0 or k > 0:
            digit = k % 10
            k //= 10
            total = carry
            if i >= 0:
                total += num[i]
                i -= 1
            total += digit
            carry = total // 10
            res.append(total % 10)
        if carry:
            res.append(carry)
        return res[::-1]
