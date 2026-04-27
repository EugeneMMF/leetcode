class Solution:
    def maxDepth(self, s: str) -> int:
        cur = maxd = 0
        for ch in s:
            if ch == '(':
                cur += 1
                if cur > maxd:
                    maxd = cur
            elif ch == ')':
                cur -= 1
        return maxd
