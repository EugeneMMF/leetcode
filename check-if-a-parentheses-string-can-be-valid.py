class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        open_min = 0
        open_max = 0
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    open_min += 1
                    open_max += 1
                else:
                    open_min -= 1
                    open_max -= 1
            else:
                open_min -= 1
                open_max += 1
            if open_max < 0:
                return False
            if open_min < 0:
                open_min = 0
        return open_min == 0