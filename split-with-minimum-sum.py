class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        a, b = [], []
        for i, d in enumerate(digits):
            if i % 2 == 0:
                a.append(d)
            else:
                b.append(d)
        return int(''.join(a)) + int(''.join(b))