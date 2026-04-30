class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        rem = n % 7
        total = 7 * (full_weeks - 1) * full_weeks // 2 + 28 * full_weeks
        total += rem * (full_weeks + 1) + rem * (rem - 1) // 2
        return total
