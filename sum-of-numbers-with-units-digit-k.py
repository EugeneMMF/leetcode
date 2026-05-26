class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            return 1 if num % 10 == 0 else -1
        for m in range(1, num // k + 1):
            remaining = num - m * k
            if remaining >= 0 and remaining % 10 == 0:
                return m
        return -1
