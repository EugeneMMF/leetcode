class Solution:
    def replaceNonCoprimes(self, nums):
        from math import gcd
        stack = []
        for x in nums:
            stack.append(x)
            while len(stack) >= 2:
                a = stack[-2]
                b = stack[-1]
                if gcd(a, b) > 1:
                    stack.pop()
                    stack.pop()
                    stack.append(a * b // gcd(a, b))
                else:
                    break
        return stack
