class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        parity = 0
        for ch in target:
            bit = int(ch)
            if parity != bit:
                flips += 1
                parity ^= 1
        return flips
