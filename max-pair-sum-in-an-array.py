from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        top = [[-1, -1] for _ in range(10)]
        for num in nums:
            m = 0
            x = num
            while x:
                d = x % 10
                if d > m:
                    m = d
                x //= 10
            a, b = top[m]
            if num >= a:
                top[m][1] = top[m][0]
                top[m][0] = num
            elif num > top[m][1]:
                top[m][1] = num
        best = -1
        for a, b in top:
            if b != -1:
                s = a + b
                if s > best:
                    best = s
        return best
