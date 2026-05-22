class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ch, cm = map(int, current.split(':'))
        dh, dm = map(int, correct.split(':'))
        cur = ch * 60 + cm
        corr = dh * 60 + dm
        diff = corr - cur
        ops = 0
        for inc in (60, 15, 5, 1):
            ops += diff // inc
            diff %= inc
        return ops
