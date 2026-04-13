class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        bal = 0
        for c in s:
            if c == '(':
                bal += 1
            else:
                bal -= 1
                if bal < 0:
                    res += 1
                    bal = 0
        return res + bal
