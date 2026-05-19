class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def rev(n):
            r = 0
            while n > 0:
                r = r * 10 + n % 10
                n //= 10
            return r
        reversed1 = rev(num)
        reversed2 = rev(reversed1)
        return reversed2 == num
