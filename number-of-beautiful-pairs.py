class Solution:
    def countBeautifulPairs(self, nums):
        import math
        n = len(nums)
        first_digits = []
        for num in nums:
            fd = num
            while fd >= 10:
                fd //= 10
            first_digits.append(fd)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if math.gcd(first_digits[i], nums[j] % 10) == 1:
                    count += 1
        return count