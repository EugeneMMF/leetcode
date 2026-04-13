class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        ones = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                flips = flips + 1 if flips + 1 < ones else ones
        return flips
