class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [c for c in number if c.isdigit()]
        res = []
        i = 0
        n = len(digits)
        while n - i > 4:
            res.append(''.join(digits[i:i+3]))
            i += 3
        remain = n - i
        if remain == 4:
            res.append(''.join(digits[i:i+2]))
            res.append(''.join(digits[i+2:i+4]))
        else:
            res.append(''.join(digits[i:]))
        return '-'.join(res)
