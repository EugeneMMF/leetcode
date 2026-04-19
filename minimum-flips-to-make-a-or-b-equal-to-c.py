class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            ai = a & 1
            bi = b & 1
            ci = c & 1
            if ci == 0:
                flips += ai + bi
            else:
                if ai == 0 and bi == 0:
                    flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
