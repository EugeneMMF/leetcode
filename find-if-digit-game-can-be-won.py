class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_single = sum(n for n in nums if n < 10)
        sum_double = sum(n for n in nums if n >= 10)
        return sum_single != sum_double