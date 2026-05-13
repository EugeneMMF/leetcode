class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = 0
        odd = -10**18
        for num in nums:
            new_even = max(even, odd + num, num)
            new_odd = max(odd, even - num)
            even, odd = new_even, new_odd
        return even