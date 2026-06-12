class Solution:
    def diagonalPrime(self, nums):
        n = len(nums)
        max_prime = 0
        for i in range(n):
            val = nums[i][i]
            if val > max_prime and self.is_prime(val):
                max_prime = val
            j = n - i - 1
            if j != i:
                val = nums[i][j]
                if val > max_prime and self.is_prime(val):
                    max_prime = val
        return max_prime

    def is_prime(self, x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True