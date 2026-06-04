class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        if digit_sum(n) <= target:
            return 0
        power = 1
        for _ in range(13):
            remainder = n % power
            delta = (power - remainder) % power
            new_n = n + delta
            if digit_sum(new_n) <= target:
                return delta
            power *= 10
        return 0