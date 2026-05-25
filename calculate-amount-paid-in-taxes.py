from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            amount = min(income, upper) - prev
            tax += amount * percent / 100.0
            prev = upper
        return tax
