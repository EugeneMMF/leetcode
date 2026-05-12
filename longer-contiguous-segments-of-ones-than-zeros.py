class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max1 = cur1 = 0
        max0 = cur0 = 0
        for ch in s:
            if ch == '1':
                cur1 += 1
                cur0 = 0
                if cur1 > max1:
                    max1 = cur1
            else:
                cur0 += 1
                cur1 = 0
                if cur0 > max0:
                    max0 = cur0
        return max1 > max0