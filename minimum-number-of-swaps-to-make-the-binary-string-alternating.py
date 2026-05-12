class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        cnt01 = cnt10 = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                if ch == '0':
                    cnt01 += 1
                else:
                    cnt10 += 1
        swaps1 = -1
        if cnt01 == cnt10:
            swaps1 = cnt01
        cnt01 = cnt10 = 0
        for i, ch in enumerate(s):
            expected = '1' if i % 2 == 0 else '0'
            if ch != expected:
                if ch == '0':
                    cnt01 += 1
                else:
                    cnt10 += 1
        swaps2 = -1
        if cnt01 == cnt10:
            swaps2 = cnt01
        if swaps1 == -1 and swaps2 == -1:
            return -1
        if swaps1 == -1:
            return swaps2
        if swaps2 == -1:
            return swaps1
        return min(swaps1, swaps2)
