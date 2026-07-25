class Solution:
    def maxLength(self, nums: List[int]) -> int:
        import math
        n = len(nums)
        best = 0
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = math.gcd(g, x)
                l = l * x // math.gcd(l, x)
                if prod == l * g:
                    best = max(best, j - i + 1)
        return best