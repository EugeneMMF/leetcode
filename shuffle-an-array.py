import random

class Solution:

    def __init__(self, nums: list[int]):
        self.original = list(nums)
        self.current = list(nums)

    def reset(self) -> list[int]:
        self.current = list(self.original)
        return self.current

    def shuffle(self) -> list[int]:
        n = len(self.current)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.current[i], self.current[j] = self.current[j], self.current[i]
        return self.current
