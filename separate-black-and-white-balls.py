class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = 0
        swaps = 0
        for ch in reversed(s):
            if ch == '0':
                zeros += 1
            else:
                swaps += zeros
        return swaps
