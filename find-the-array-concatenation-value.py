class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        total = 0
        pow10 = [1, 10, 100, 1000, 10000, 100000]
        while l < r:
            b = nums[r]
            digits = 1
            if b >= 10000:
                digits = 5
            elif b >= 1000:
                digits = 4
            elif b >= 100:
                digits = 3
            elif b >= 10:
                digits = 2
            total += nums[l] * pow10[digits] + b
            l += 1
            r -= 1
        if l == r:
            total += nums[l]
        return total
