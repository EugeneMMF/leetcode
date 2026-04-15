class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        while target > startValue:
            ops += 1
            if target % 2:
                target += 1
            else:
                target //= 2
        return ops + (startValue - target)
