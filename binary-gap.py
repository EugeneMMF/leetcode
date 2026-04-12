class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last = -1
        pos = 0
        while n:
            if n & 1:
                if last != -1:
                    gap = pos - last
                    if gap > max_gap:
                        max_gap = gap
                last = pos
            n >>= 1
            pos += 1
        return max_gap
